from datetime import datetime
from fastapi import APIRouter, HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import create_access_token
import jwt
from rsa import verify
from jwt import verify_access_token
from jwt import ALGORITHM, JWT_SECRET_KEY
from user import NewShipment,Shipments
from config import Hash
from user import User,Login
from db import conn,collection_name
from schema import userEntity,usersEntity
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
   return verify_access_token(access_token)
   

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
    
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = (token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user


# def authenticate_user(username, password):
#     try:
#         user = json.loads(User.objects.get(username=username).to_json())
#         return verify(password, user['password'])
#     except User.DoesNotExist:
#         return False   
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@user.post("/add_shipment")
def add_shipment(shipment: NewShipment):
   new_shipment= collection_name.insert_one(shipment)
   return {"message": new_shipment}
    # try:
    #     payload = jwt.decode(
    #         token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
    #     )

    #     # token_data = verify_access_token(**payload)

    #     if datetime.fromtimestamp(payload['exp']) < datetime.now():
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail="Token expired",
    #             headers={"WWW-Authenticate": "Bearer"},
    #         )
    # except(jwt.JWTError):
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
        
    # new_shipment = Shipments(Invoice_no=shipment.Invoice_no,
    #                          container_no=shipment.container_no,
    #                          shipment_description=shipment.shipment_description,
    #                          route_details=shipment.route_details,
    #                          goods_type=shipment.goods_type,
    #                          device=shipment.device,
    #                          expected_delivery_date=shipment.expected_delivery_date,
    #                          PO_number=shipment.PO_number,
    #                          delivery_no=shipment.delivery_no,
    #                          NDC_no=shipment.NDC_no,
    #                          batch_id=shipment.batch_id,
    #                          Serial_no_of_goods=shipment.Serial_no_of_goods
    #                          )
    # new_shipment.save()




     
    
        
