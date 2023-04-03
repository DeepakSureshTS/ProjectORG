from config import Hash
from db import collection_device, collection_name, collection_shipment
from fastapi import APIRouter, Depends, HTTPException, status
from jwt import create_access_token, get_current_user
from schema import devices_entity
from user import Login, NewShipment, User
from validation import validation

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

   access_token = create_access_token(data={"LoggedUsername":user_data["username"]})
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
    return{"message": "created new user"}


@user.get("/token_authentication")
def validity_check(token: str = Depends(get_current_user)):
    if token:
        return {"TokenDetails":token}
    
        
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

@user.get("/devicestream")
def device_data(token: str = Depends(get_current_user)):
   if token:
       return devices_entity(collection_device.find())

   
  



     
    
        
