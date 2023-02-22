from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from user import TokenData


SECRET_KEY = "2612d2f66bfe9a9c4a0ed25be92a29f7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
JWT_SECRET_KEY = "2fcb3d895799b8d8fe953b184d3c757d21c60514db6c62455f816939a2ff8703"

def create_access_token(data:dict):
    to_encode =data.copy()
    expire =datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

# def verify_access_token(token:str):
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
def verify_access_token(token: str):
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
     
    return verify_access_token(token)
