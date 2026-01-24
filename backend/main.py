from fastapi import FastAPI
from models import Register


app = FastAPI()

@app.post("/users/")
def read_user(user : Register):
    return {"user is successfully created" : user}

@app.get("/users/{user}")
def get_user(user: str):
    return {"user": user}