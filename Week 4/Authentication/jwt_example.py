from jose import jwt

SECRET="secret123"

data={

"user":"Barani"

}

token=jwt.encode(

data,

SECRET,

algorithm="HS256"

)

print(token)