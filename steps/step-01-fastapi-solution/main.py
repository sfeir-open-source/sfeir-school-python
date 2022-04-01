from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def startup():
    print("Okay, let's go !")

@app.on_event("shutdown")
def shutdown():
    print("Bye Bye...")

@app.get("/")
def root():
    return {"message": "Hello world!"}
