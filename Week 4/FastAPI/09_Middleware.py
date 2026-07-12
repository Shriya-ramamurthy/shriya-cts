from fastapi import Request

@app.middleware("http")

async def middleware(

request:Request,

call_next

):

    print("Before Request")

    response=await call_next(request)

    print("After Response")

    return response