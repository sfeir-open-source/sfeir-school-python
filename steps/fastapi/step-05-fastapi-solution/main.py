import datetime

from fastapi import FastAPI, HTTPException
from databases import Database
from pydantic import BaseModel


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


database = Database("sqlite:///test.db")

app = FastAPI()


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


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
async def get_all_messages() -> [MessageGet]:
    query = f"SELECT * FROM messages"
    results = await database.fetch_all(query=query)
    return results


@app.put("/message/{message_id}")
async def update_message(message_id, messageUpdated: MessageUpdate) -> MessageGet:
    query = f"UPDATE messages SET message = '{messageUpdated.message}' WHERE id = '{message_id}'"
    updated_id = await database.execute(query=query)
    return await get_message(updated_id)


@app.delete("/message/{message_id}")
async def delete_message(message_id):
    query = f"DELETE FROM messages WHERE id = '{message_id}'"
    deleted_id = await database.execute(query=query)
    return deleted_id
