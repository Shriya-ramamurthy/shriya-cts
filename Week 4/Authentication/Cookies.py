from fastapi import Response

@app.get("/cookie")

def cookie(

response:Response

):

    response.set_cookie(

        key="username",

        value="Barani"

    )

    return {

        "Cookie":"Created"

    }