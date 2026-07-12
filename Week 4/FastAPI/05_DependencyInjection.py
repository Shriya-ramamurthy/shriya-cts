from fastapi import Depends

def get_db():

    return "Database Connected"

@app.get("/database")

def database(

db=Depends(get_db)

):

    return {

        "db":db

    }