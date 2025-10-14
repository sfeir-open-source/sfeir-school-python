import datetime

from fastapi import FastAPI, HTTPException
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
    await database.connect()
    try:
        yield
    finally:
        await database.disconnect()


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/message/{message_id}")
async def get_message(message_id: int) -> MessageGet:
    query = "SELECT * FROM messages WHERE id={}".format(message_id)
    result = await database.fetch_one(query=query)
    if not result:
      raise HTTPException(status_code=404, detail="Message not found")
    return result


@app.post("/message")
async def create_message(message: MessagePost) -> MessageGet:
  query = f"INSERT INTO messages (author, message) VALUES ('{message.author}', '{message.message}')"
  created_id = await database.execute(query)
  return await get_message(created_id)

@app.get("/messages")
async def get_all_messages() -> list[MessageGet]:
  pass

@app.put("/message/{message_id}")
async def update_message(message_id, messageUpdated: MessageUpdate) -> MessageGet:
  pass

@app.delete("/message/{message_id}")
async def delete_message(message_id):
  pass
