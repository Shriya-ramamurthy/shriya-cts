from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt

# Secret key and algorithm for JWT encoding/decoding
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="JWT Auth API")

# Setup OAuth2 token URL endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Mock user database
fake_users_db = {
    "john_doe": {
        "username": "john_doe",
        "password": "secretpassword", # Plaintext for example purposes
    }
}

# Helper functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return fake_users_db[username]
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")


# 1. Login Route (Generates JWT)
@app.post("/login", tags=["Auth"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


# 2. Protected Route (Requires valid JWT in Header)
@app.get("/users/me", tags=["Protected"])
def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"], "message": "Access granted to protected route!"}


# 3. Logout Route
@app.post("/logout", tags=["Auth"])
def logout():
    # Stateless JWTs cannot be invalidated server-side without a revocation list/database.
    # Front-end simply deletes the stored token.
    return {"message": "Successfully logged out. Please remove the token from client storage."}
