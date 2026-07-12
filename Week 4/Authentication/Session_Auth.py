from fastapi import FastAPI

app=FastAPI()

sessions={}

@app.post("/login")

def login(username:str):

    sessions["user"]=username

    return {

        "message":"Logged In"

    }

@app.get("/profile")

def profile():

    return sessions