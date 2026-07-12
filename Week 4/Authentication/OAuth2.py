from fastapi.security import OAuth2PasswordBearer

oauth2_scheme=OAuth2PasswordBearer(

tokenUrl="login"

)


from fastapi import Depends

@app.get("/dashboard")

def dashboard(

token:str=Depends(

oauth2_scheme

)

):

    return {

        "token":token

    }