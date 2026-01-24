from fastapi import FastAPI
import models


app = FastAPI()


@app.get("/models/{user}")
def read_user(user: models.register):
    return user