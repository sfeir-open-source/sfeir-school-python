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
    creation_date: datetime = Field(default_factory=lambda: datetime.now(UTC))


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
    message = Message.model_validate(message_in)
    session.add(message)
    await session.commit()
    # refresh recharge l'objet depuis la base, pour récupérer l'id généré
    await session.refresh(message)
    return message


@app.get("/messages/{message_id}", response_model=MessagePublic)
async def read_message(session: SessionDep, message_id: int) -> Message:
    message = await session.get(Message, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


@app.get("/messages", response_model=list[MessagePublic])
async def list_messages(session: SessionDep) -> list[Message]:
    # order_by(id) : l'ordre reste le même d'une requête à l'autre
    result = await session.exec(select(Message).order_by(Message.id))
    return result.all()


@app.patch("/messages/{message_id}", response_model=MessagePublic)
async def update_message(
    session: SessionDep, message_id: int, message_in: MessageUpdate
) -> Message:
    message = await session.get(Message, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    # exclude_unset : seuls les champs envoyés par le client sont modifiés
    # exclude_none : "message": null n'efface pas le texte (la colonne est obligatoire)
    message.sqlmodel_update(message_in.model_dump(exclude_unset=True, exclude_none=True))
    session.add(message)
    await session.commit()
    await session.refresh(message)
    return message


@app.delete("/messages/{message_id}", status_code=204)
async def delete_message(session: SessionDep, message_id: int) -> None:
    message = await session.get(Message, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    await session.delete(message)
    await session.commit()
