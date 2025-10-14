from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code à exécuter au démarrage
    print("Okay, let's go !")
    try:
        yield
    finally:
        # Code à exécuter à l'arrêt
        print("Bye Bye...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello world!"}
