from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from jwt import get_current_user




from config import Hash
from db import collection_name,collection_shipment
from jwt import (ALGORITHM, create_access_token,
                 verify_access_token)
from schema import userEntity, usersEntity,shipsEntity
from user import Login, NewShipment, User

user= APIRouter()

@user.post('/login')
async def find_users(user:Login):
   
   user_data= collection_name.find_one({"email":user.email})
 
   if not user_data:
     return {
        "error":"email not found"
     }
   if not Hash.verify(user.password,user_data["password"]) :
       return{
        "error":" password mismatch"
       }

   access_token = create_access_token(data={"token":user_data["email"]})
   return {"access_token": access_token, 
   "token_type": "bearer"}
   

@user.post('/signup')
async def create_user(user:User):
    email_check= collection_name.find_one({"email":user.email})
   #  validate_password = pass_validation(user)
    if email_check:
        return{
            "error":"email already found"
        }  
    else: 
     hashed_pass= Hash.bcrypt(user.password)
     user.password= hashed_pass
     collection_name.insert_one(dict(user))
    # return usersEntity(collection_name.find())
    return{"message": "created new user"}

@user.get("/dashboard")
def validity_check(token: str = Depends(get_current_user)):
    if token:
        return True

       

@user.post("/add_shipment")
def add_shipment(shipment: NewShipment,token: Login = Depends(get_current_user)):
    if token:
        collection_shipment.insert_one(dict(shipment))
        return {"message": "created successfully","Loggedemail":token}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED(
                detail="User not Authenticated. Please log first."
            )
        )
#  return shipsEntity(collection_shipment.find())
  



     
    
        
