from fastapi import APIRouter, Depends, HTTPException, status
from validation import validation
from jwt import get_current_user
from config import Hash
from db import collection_name,collection_shipment
from jwt import (create_access_token)

from user import Login, NewShipment, User

user= APIRouter()

@user.post('/login')
async def find_users(user:Login):
   
   user_data= collection_name.find_one({"email":user.email})
 
   if not user_data:
     raise HTTPException(
        status_code=400,detail= "Email not Found"
     )
   if not Hash.verify(user.password,user_data["password"]) :
      raise HTTPException(
        status_code=400,detail= "Password mismatch"
     )

   access_token = create_access_token(data={"token":user_data["email"]})
   return {"access_token": access_token,"token_type": "bearer"}


@user.post('/signup')
async def create_user(user:User):
    email_check= collection_name.find_one({"email":user.email})
    
    validation(user)

    if email_check:
       
     raise HTTPException(
        status_code=400,detail= "email already found"
     )
    else: 
     hashed_pass= Hash.bcrypt(user.password)
     user.password= hashed_pass
     collection_name.insert_one(dict(user))
    # return usersEntity(collection_name.find())
    return{"message": "created new user"}


@user.get("/token_authentication")
def validity_check(token: str = Depends(get_current_user)):
    if token:
        return {"Loggedemail":token}
    
        
@user.post("/add_shipment")
def add_shipment(shipment: NewShipment,token: Login = Depends(get_current_user)):
    if token:
        collection_shipment.insert_one(dict(shipment))
        return {"message": "created successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED(
                detail="User not Authenticated. Please log first."
            )
        )
#  return shipsEntity(collection_shipment.find())
  



     
    
        
