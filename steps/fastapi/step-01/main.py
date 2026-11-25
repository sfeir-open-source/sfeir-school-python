"""Lab step-01 : une API de messages, sans base de données (20-25 minutes).

Complétez les TODO, puis vérifiez avec :
    uv run pytest -q --tb=short steps/fastapi/step-01
Lancez l'application avec :
    uv run fastapi dev steps/fastapi/step-01/main.py     puis ouvrez http://127.0.0.1:8000/docs
"""

from datetime import UTC, datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- Modèles -----------------------------------------------------------------


class MessageCreate(BaseModel):
    # Ce que le client envoie pour créer un message
    # TODO : author (str, de 1 à 50 caractères) et message (str, de 1 à 500 caractères)
    #        avec Field(min_length=..., max_length=...)
    pass


class MessagePublic(MessageCreate):
    # Ce que l'API renvoie : les champs de MessageCreate, plus l'id et la date
    # TODO : ajouter id (int) et creation_date (datetime)
    pass


# --- Application -------------------------------------------------------------

app = FastAPI(title="Messages API")

# "Base de données" en mémoire : identifiant -> message. Perdue à chaque redémarrage.
messages: dict[int, MessagePublic] = {}


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.post("/messages", status_code=201)
async def create_message(message_in: MessageCreate) -> MessagePublic:
    # TODO : construire un MessagePublic avec id=len(messages) + 1, creation_date=datetime.now(UTC)
    #        et les champs de message_in (message_in.model_dump()), le ranger dans messages
    #        sous son id, puis le renvoyer
    raise NotImplementedError


@app.get("/messages/{message_id}")
async def read_message(message_id: int) -> MessagePublic:
    # TODO : renvoyer le message, ou lever
    #        HTTPException(status_code=404, detail="Message not found")
    raise NotImplementedError


@app.get("/messages")
async def list_messages() -> list[MessagePublic]:
    # TODO : renvoyer tous les messages sous forme de liste
    raise NotImplementedError
