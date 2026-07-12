from passlib.context import CryptContext

pwd=CryptContext(

schemes=["bcrypt"]

)

password=pwd.hash(

"admin123"

)

print(password)