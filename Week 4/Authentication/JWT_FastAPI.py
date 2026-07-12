from fastapi import FastAPI

from jose import jwt

app=FastAPI()

SECRET="secret123"

@app.post("/login")

def login():

    token=jwt.encode(

        {

            "user":"Barani"

        },

        SECRET,

        algorithm="HS256"

    )

    return {

        "token":token

    }