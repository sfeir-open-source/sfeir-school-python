from datetime import UTC, datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- Modèles -----------------------------------------------------------------


class MessageCreate(BaseModel):
    # Ce que le client envoie pour créer un message
    author: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=500)


class MessagePublic(MessageCreate):
    # Ce que l'API renvoie : les champs de MessageCreate, plus l'id et la date
    id: int
    creation_date: datetime


# --- Application -------------------------------------------------------------

app = FastAPI(title="Messages API")

# "Base de données" en mémoire : identifiant -> message. Perdue à chaque redémarrage.
messages: dict[int, MessagePublic] = {}


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.post("/messages", status_code=201)
async def create_message(message_in: MessageCreate) -> MessagePublic:
    message = MessagePublic(
        id=len(messages) + 1,
        creation_date=datetime.now(UTC),
        **message_in.model_dump(),
    )
    messages[message.id] = message
    return message


@app.get("/messages/{message_id}")
async def read_message(message_id: int) -> MessagePublic:
    if message_id not in messages:
        raise HTTPException(status_code=404, detail="Message not found")
    return messages[message_id]


@app.get("/messages")
async def list_messages() -> list[MessagePublic]:
    return list(messages.values())
