from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):

    name:str

    age:int

@app.get(

"/student",

response_model=Student

)

def get():

    return {

        "name":"Barani",

        "age":21

    }