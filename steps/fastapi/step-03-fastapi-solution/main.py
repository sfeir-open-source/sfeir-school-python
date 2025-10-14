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
    await database.connect()
    try:
        yield
    finally:
        await database.disconnect()

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/health")
async def check_database_health(response: Response):
    if database.is_connected:
        response.status_code = 200
        return {"message": "Database is connected"}
    response.status_code = 500
    raise {"message": "Database is not connected"}


@app.get("/tables")
async def get_database_tables(response: Response):
    if not database.is_connected:
        response.status_code = 500
        raise {"message": "Database is not connected"}
    query = f"SELECT name FROM sqlite_master WHERE type='table'"
    results = await database.fetch_all(query=query)
    return results
