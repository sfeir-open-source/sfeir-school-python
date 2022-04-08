from fastapi import FastAPI, Response
from databases import Database
from pydantic import BaseModel


class MessagePost(BaseModel):
    pass


class MessageUpdate(BaseModel):
    pass


class MessageGet(BaseModel):
    pass


database = Database("sqlite:///../test.db")

app = FastAPI()


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/health")
def check_database_health(response: Response):
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
