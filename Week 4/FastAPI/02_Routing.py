from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def students():
    return ["Barani","John","Arun"]

@app.post("/students")
def add_student():
    return {"message":"Student Added"}

@app.put("/students/{id}")
def update_student(id:int):
    return {"id":id}

@app.delete("/students/{id}")
def delete_student(id:int):
    return {"deleted":id}