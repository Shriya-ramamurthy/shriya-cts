from fastapi import HTTPException

@app.get("/student/{id}")

def student(id:int):

    if id!=1:

        raise HTTPException(

            status_code=404,

            detail="Student Not Found"

        )

    return {

        "Student":id

    }