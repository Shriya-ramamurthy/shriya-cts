from fastapi import FastAPI

app=FastAPI()

@app.get("/student/{id}")
def student(id:int):

    return {

        "Student ID":id

    }
    
    
    @app.get("/search")

def search(

name:str,

age:int

):

    return {

        "Name":name,

        "Age":age

    }