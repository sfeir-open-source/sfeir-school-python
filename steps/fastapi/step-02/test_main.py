import importlib.util
import sys
from collections.abc import AsyncGenerator
from datetime import datetime
from pathlib import Path

import httpx
import pytest
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

pytestmark = pytest.mark.anyio


def load_main():
    # Charge le main.py de CE dossier sous un nom unique : plusieurs étapes sont testées ensemble
    path = Path(__file__).resolve().parent / "main.py"
    name = f"main_{path.parent.name.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# SQLModel.metadata est global : on repart d'un registre vide avant de charger CE main.py
SQLModel.metadata.clear()
main = load_main()
# Tables déclarées par CE main.py uniquement
TABLES = list(SQLModel.metadata.sorted_tables)


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client() -> AsyncGenerator[httpx.AsyncClient]:
    # Base SQLite en mémoire : les tests n'écrivent jamais dans steps/fastapi/messages.db
    engine = create_async_engine("sqlite+aiosqlite://", poolclass=StaticPool)
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all, tables=TABLES)

    async def override_get_session() -> AsyncGenerator[AsyncSession]:
        async with AsyncSession(engine) as session:
            yield session

    main.app.dependency_overrides[main.get_session] = override_get_session
    # ASGITransport appelle l'application sans lancer le lifespan : messages.db n'est pas touché
    transport = httpx.ASGITransport(app=main.app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
    main.app.dependency_overrides.clear()
    await engine.dispose()


# --- Validation des modèles (sans base de données) ---------------------------


def test_message_create_valid():
    message = main.MessageCreate(author="Alice", message="Bonjour")
    assert message.author == "Alice"


def test_author_cannot_be_empty():
    with pytest.raises(ValidationError):
        main.MessageCreate(author="", message="Bonjour")


def test_message_table_has_creation_date():
    message = main.Message(author="Alice", message="Bonjour")
    assert isinstance(message.creation_date, datetime)


# --- Création et lecture ----------------------------------------------------


async def test_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


async def test_create_message_returns_201(client):
    response = await client.post("/messages", json={"author": "Alice", "message": "Bonjour"})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["author"] == "Alice"
    assert body["message"] == "Bonjour"
    assert "creation_date" in body


async def test_get_message_returns_the_created_message(client):
    created = (await client.post("/messages", json={"author": "Alice", "message": "Salut"})).json()
    response = await client.get(f"/messages/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


async def test_get_unknown_message_returns_404(client):
    response = await client.get("/messages/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Message not found"


async def test_apostrophe_is_stored_as_text(client):
    response = await client.post("/messages", json={"author": "Bob", "message": "l'API c'est top"})
    assert response.status_code == 201
    assert response.json()["message"] == "l'API c'est top"


async def test_empty_author_returns_422(client):
    response = await client.post("/messages", json={"author": "", "message": "Bonjour"})
    assert response.status_code == 422
    error = response.json()["detail"][0]
    assert error["type"] == "string_too_short"
    assert error["loc"] == ["body", "author"]


# --- Liste, modification, suppression ----------------------------------------


async def create_messages(client, count):
    return [
        (await client.post("/messages", json={"author": "Alice", "message": f"Message {i}"})).json()
        for i in range(count)
    ]


async def test_list_messages_ordered_by_id(client):
    created = await create_messages(client, 3)
    response = await client.get("/messages")
    assert response.status_code == 200
    assert [m["id"] for m in response.json()] == [m["id"] for m in created]


async def test_patch_updates_only_the_message_field(client):
    created = (await create_messages(client, 1))[0]
    response = await client.patch(f"/messages/{created['id']}", json={"message": "Modifié"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["message"] == "Modifié"
    assert updated["author"] == created["author"]
    assert updated["creation_date"] == created["creation_date"]


async def test_patch_unknown_message_returns_404(client):
    response = await client.patch("/messages/999", json={"message": "Modifié"})
    assert response.status_code == 404


async def test_delete_message_returns_204(client):
    created = (await create_messages(client, 1))[0]
    response = await client.delete(f"/messages/{created['id']}")
    assert response.status_code == 204
    assert (await client.get(f"/messages/{created['id']}")).status_code == 404


async def test_delete_unknown_message_returns_404(client):
    response = await client.delete("/messages/999")
    assert response.status_code == 404
