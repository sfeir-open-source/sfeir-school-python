import importlib.util
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError


def load_main():
    # Charge le main.py de CE dossier sous un nom unique : plusieurs étapes sont testées ensemble
    path = Path(__file__).resolve().parent / "main.py"
    name = f"main_{path.parent.name.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


main = load_main()


@pytest.fixture
def client():
    # Les messages sont gardés en mémoire : on repart d'un dictionnaire vide à chaque test
    main.messages.clear()
    return TestClient(main.app)


# --- Validation des modèles (sans serveur) -----------------------------------


def test_message_create_valid():
    message = main.MessageCreate(author="Alice", message="Bonjour")
    assert message.author == "Alice"
    assert message.message == "Bonjour"


def test_author_cannot_be_empty():
    with pytest.raises(ValidationError):
        main.MessageCreate(author="", message="Bonjour")


def test_author_max_50_characters():
    with pytest.raises(ValidationError):
        main.MessageCreate(author="a" * 51, message="Bonjour")


def test_message_max_500_characters():
    with pytest.raises(ValidationError):
        main.MessageCreate(author="Alice", message="a" * 501)


def test_message_public_has_id_and_creation_date():
    assert {"id", "creation_date"} <= set(main.MessagePublic.model_fields)


# --- Routes ------------------------------------------------------------------


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_create_message_returns_201(client):
    response = client.post("/messages", json={"author": "Alice", "message": "Bonjour"})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["author"] == "Alice"
    assert body["message"] == "Bonjour"
    assert "creation_date" in body


def test_get_message_returns_the_created_message(client):
    created = client.post("/messages", json={"author": "Alice", "message": "Salut"}).json()
    response = client.get(f"/messages/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_get_unknown_message_returns_404(client):
    response = client.get("/messages/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Message not found"


def test_list_messages_in_creation_order(client):
    for i in range(3):
        client.post("/messages", json={"author": "Alice", "message": f"Message {i}"})
    response = client.get("/messages")
    assert response.status_code == 200
    assert [m["message"] for m in response.json()] == ["Message 0", "Message 1", "Message 2"]


def test_empty_author_returns_422(client):
    response = client.post("/messages", json={"author": "", "message": "Bonjour"})
    assert response.status_code == 422
    error = response.json()["detail"][0]
    assert error["type"] == "string_too_short"
    assert error["loc"] == ["body", "author"]


def test_get_with_non_integer_id_returns_422(client):
    response = client.get("/messages/abc")
    assert response.status_code == 422
