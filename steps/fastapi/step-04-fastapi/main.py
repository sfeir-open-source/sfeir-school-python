import datetime

from fastapi import FastAPI, Response
from databases import Database
from pydantic import BaseModel
from contextlib import asynccontextmanager


class MessagePost(BaseModel):
    author: str
    message: str


class MessageUpdate(BaseModel):
    message: str


class MessageGet(BaseModel):
    id: int
    author: str
    message: str
    creation_date: datetime.datetime


database = Database("sqlite:///../test.db")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code à exécuter au démarrage
    await database.connect()
    print("Connexion à la base de données établie.")
    try:
        yield
    finally:
        # Code à exécuter à l'arrêt
        await database.disconnect()
        print("Connexion à la base de données fermée.")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/message/{message_id}")
async def get_message(message_id: int) -> MessageGet:
    pass


@app.post("/message")
async def create_message(message: MessagePost) -> MessageGet:
    pass
