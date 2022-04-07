import datetime

from fastapi import FastAPI, HTTPException, Response
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


class AuthorStats(BaseModel):
    pass


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


@app.get("/author/{author_name}/messages")
async def get_all_messages_from_author(author, response: Response) -> [MessageGet]:
    response.status_code = 501


@app.get("/stats")
async def get_messages_stats(response: Response) -> [AuthorStats]:
    """
    It's up to you but here are some ideas :
    - min, max and average length of message
    - min, max and average number of messages per author
    - min, max and average number of messages per day or hour
    - etc
    """
    response.status_code = 501


@app.get("/author/{author_name}/stats")
async def get_messages_stats_for_author(author, response: Response) -> [AuthorStats]:
    response.status_code = 501


@app.post("/generate")
async def generate_messages_for_databse(response: Response):
    """
    This goal of this function is to generate automatically many messages
    (10 ? 100 ? 1000 ?) and to push them into the database.

    So instead of creating message manually, we can call this function and we have enough data
    for stats routes.
    """
    response.status_code = 501