from passlib.context import CryptContext

pwd_encode=CryptContext(schemes=["bcrypt"],deprecated="auto")


class Hash:
    def bcrypt(password:str):
        return pwd_encode.hash(password)

    def verify(normal,hashed):
        return pwd_encode.verify(normal, hashed)
