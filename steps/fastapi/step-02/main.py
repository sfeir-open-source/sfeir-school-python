"""Lab step-02 : les messages dans une base SQLite, avec SQLModel (20-25 minutes).

Le moteur, la session (dépendance) et la création des tables sont fournis.
Complétez les TODO, puis vérifiez avec :
    uv run pytest -q --tb=short steps/fastapi/step-02
Lancez l'application avec :
    uv run fastapi dev steps/fastapi/step-02/main.py     puis ouvrez http://127.0.0.1:8000/docs
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

# --- Modèles -----------------------------------------------------------------
# Un seul modèle sert à la fois de validation (Pydantic) et de table SQL (SQLModel)


class MessageBase(SQLModel):
    # Champs communs aux modèles d'entrée et de sortie
    author: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=500)


class Message(MessageBase, table=True):
    # table=True : ce modèle correspond à la table SQL "message"
    # id reste None tant que la base n'a pas attribué d'identifiant
    id: int | None = Field(default=None, primary_key=True)
    # TODO : ajouter creation_date (datetime), avec la date UTC du moment pour valeur par défaut :
    #        Field(default_factory=lambda: datetime.now(UTC))


class MessageCreate(MessageBase):
    # Ce que le client envoie pour créer un message
    pass


class MessagePublic(MessageBase):
    # Ce que l'API renvoie au client : on expose l'id et la date
    id: int
    creation_date: datetime


class MessageUpdate(SQLModel):
    # Tous les champs sont optionnels : on ne modifie que ce qui est envoyé
    message: str | None = Field(default=None, min_length=1, max_length=500)


# --- Base de données ---------------------------------------------------------

# Fichier SQLite partagé avec le lab MCP : steps/fastapi/messages.db
DB_PATH = Path(__file__).resolve().parents[1] / "messages.db"
# En production, seule cette URL change (par exemple "postgresql+asyncpg://...")
engine = create_async_engine(f"sqlite+aiosqlite:///{DB_PATH}")


async def get_session() -> AsyncGenerator[AsyncSession]:
    # Une session par requête, fermée automatiquement à la fin de la requête
    async with AsyncSession(engine) as session:
        yield session


# Dépendance réutilisable : déclarer `session: SessionDep` dans une route suffit
SessionDep = Annotated[AsyncSession, Depends(get_session)]


async def create_tables() -> None:
    # Crée les tables déclarées avec SQLModel (si elles n'existent pas)
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Au démarrage de l'application
    await create_tables()
    yield


app = FastAPI(title="Messages API", lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.post("/messages", status_code=201, response_model=MessagePublic)
async def create_message(session: SessionDep, message_in: MessageCreate) -> Message:
    # TODO : Message.model_validate(message_in), session.add(...), await session.commit(),
    #        await session.refresh(...) pour récupérer l'id, puis renvoyer le message
    raise NotImplementedError


@app.get("/messages/{message_id}", response_model=MessagePublic)
async def read_message(session: SessionDep, message_id: int) -> Message:
    # TODO : await session.get(Message, message_id), ou 404 "Message not found" s'il est absent
    raise NotImplementedError


@app.get("/messages", response_model=list[MessagePublic])
async def list_messages(session: SessionDep) -> list[Message]:
    # TODO : result = await session.exec(select(Message).order_by(Message.id)), puis result.all()
    raise NotImplementedError


# --- Pour les plus rapides : modifier et supprimer ---------------------------


@app.patch("/messages/{message_id}", response_model=MessagePublic)
async def update_message(
    session: SessionDep, message_id: int, message_in: MessageUpdate
) -> Message:
    # TODO : chercher le message (404 "Message not found" si absent), l'appliquer avec
    #        message.sqlmodel_update(message_in.model_dump(exclude_unset=True, exclude_none=True)),
    #        puis add, commit, refresh et renvoyer le message
    raise NotImplementedError


@app.delete("/messages/{message_id}", status_code=204)
async def delete_message(session: SessionDep, message_id: int) -> None:
    # TODO : chercher le message (404 si absent), puis await session.delete(message) et commit
    raise NotImplementedError
