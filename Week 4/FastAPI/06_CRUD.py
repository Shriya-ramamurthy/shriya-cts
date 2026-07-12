students=[]
@app.post("/students")

def add(

student:Student

):

    students.append(student)

    return student
@app.get("/students")

def get():

    return students
@app.put("/students/{id}")

def update(

id:int,

student:Student

):

    students[id]=student

    return student
@app.delete("/students/{id}")

def delete(

id:int

):

    students.pop(id)

    return {

        "Deleted":id

    }