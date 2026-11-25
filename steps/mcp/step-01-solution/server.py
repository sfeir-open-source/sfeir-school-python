"""Lab MCP : un serveur qui expose l'API de messages (corrigé).

Les docstrings des tools, de la resource et du prompt sont lues par le LLM :
elles sont donc en anglais (les modèles y sont plus à l'aise), le reste du code
est commenté en français.

La base est celle du lab FastAPI (steps/fastapi/messages.db) ; elle est créée
au démarrage si elle n'existe pas encore.
"""

import json
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pydantic import ValidationError
from sqlalchemy import Engine
from sqlmodel import Field, Session, SQLModel, col, create_engine, select

# --- Fourni : modèles, base de données et fonctions d'accès -------------------------------


class MessageBase(SQLModel):
    author: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=500)


class Message(MessageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=lambda: datetime.now(UTC))


# parents[0] = step-01, parents[1] = mcp, parents[2] = steps
DB_PATH = Path(__file__).resolve().parents[2] / "fastapi" / "messages.db"
# check_same_thread=False : FastMCP peut exécuter les tools dans un autre thread.
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})


def init_db(target: Engine | None = None) -> None:
    """Crée les tables si elles n'existent pas encore."""
    SQLModel.metadata.create_all(target or engine)


def _latest_messages(limit: int) -> list[dict]:
    """Les `limit` messages les plus récents, du plus récent au plus ancien."""
    with Session(engine) as session:
        statement = select(Message).order_by(col(Message.id).desc()).limit(limit)
        return [m.model_dump(mode="json") for m in session.exec(statement)]


def _find_message(message_id: int) -> dict | None:
    """Le message d'identifiant `message_id`, ou None s'il n'existe pas."""
    with Session(engine) as session:
        message = session.get(Message, message_id)
        return message.model_dump(mode="json") if message else None


def _save_message(author: str, message: str) -> dict:
    """Enregistre un message et le renvoie, avec son id et sa date de création."""
    try:
        data = MessageBase(author=author, message=message)
    except ValidationError as exc:
        raise ToolError(
            "Données invalides : l'auteur fait de 1 à 50 caractères, "
            "le message de 1 à 500 caractères."
        ) from exc
    with Session(engine) as session:
        record = Message(**data.model_dump())
        session.add(record)
        session.commit()
        session.refresh(record)
        return record.model_dump(mode="json")


# --- Le serveur MCP -------------------------------------------------------------------------

# Le nom du serveur apparaît dans l'inspecteur et dans l'agent.
mcp = FastMCP("messages")


# Exercice 1 : tools simples (décorateur, docstring, type hints)
@mcp.tool
def count_words(text: str) -> int:
    # Docstring en anglais : elle dit au LLM quand utiliser ce tool
    """Count the words in a text. Use it when the user asks how many words a text contains."""
    return len(text.split())  # le nombre de mots du texte


@mcp.tool
def now(timezone: str = "Europe/Paris") -> str:
    # Docstring en anglais : elle dit au LLM quand utiliser ce tool
    """Return the current date and time as an ISO 8601 string in an IANA timezone.
    Use it when the user asks what time or day it is."""
    return datetime.now(ZoneInfo(timezone)).isoformat(timespec="seconds")  # l'heure dans ce fuseau


# Exercice 2 : tools sur les messages (ToolError, requête avec contains)
@mcp.tool
def list_messages(limit: int = 10) -> list[dict]:
    """List the most recent messages of the guestbook, newest first.
    Use it to see what people wrote recently. `limit` is the maximum number of messages."""
    return _latest_messages(limit)  # exemple fourni


@mcp.tool
def get_message(message_id: int) -> dict:
    """Get one message by its numeric id. Use it when you already know the id of a message."""
    message = _find_message(message_id)  # None si le message n'existe pas
    if message is None:
        # Ce texte est renvoyé à l'agent, qui peut le lire et corriger son appel.
        raise ToolError(f"Aucun message avec l'identifiant {message_id}.")
    return message


@mcp.tool
def post_message(author: str, message: str) -> dict:
    """Post a new message in the guestbook and return it, with its id and creation date.
    Use it only when the user explicitly asks to write or post a message."""
    return _save_message(author, message)  # enregistre le message et le renvoie


@mcp.tool
def search_messages(query: str, limit: int = 10) -> list[dict]:
    """Search the guestbook for messages whose text contains `query`, newest first.
    Use it to find messages about a topic or containing a keyword."""
    with Session(engine) as session:
        statement = (
            select(Message)
            .where(col(Message.message).contains(query))  # contains : jamais de f-string en SQL
            .order_by(col(Message.id).desc())
            .limit(limit)
        )
        return [m.model_dump(mode="json") for m in session.exec(statement)]


# Exercice 3 : une resource et un prompt
@mcp.resource("messages://latest", mime_type="application/json")
def latest_messages_resource() -> str:
    """The 5 most recent messages, as JSON. Read it to get a quick overview of the guestbook."""
    return json.dumps(_latest_messages(5), ensure_ascii=False)  # les 5 derniers, en JSON


@mcp.prompt
def summarize_messages(limit: int = 20) -> str:
    """Ask the assistant to summarise the latest messages of the guestbook."""
    return (
        f"Use the list_messages tool to fetch the {limit} most recent messages. "
        "Then write a short summary in French: the main topics, who wrote what, "
        "and anything that seems to need an answer."
    )


if __name__ == "__main__":
    # Crée messages.db et les tables si besoin, puis lance le serveur en stdio.
    # En stdio, stdout est le canal du protocole : n'y écrivez jamais avec print().
    init_db()
    mcp.run()
