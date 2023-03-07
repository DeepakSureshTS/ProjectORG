from pydantic import BaseModel

class User(BaseModel):
    username:str 
    email:str 
    password:str 

class Login(BaseModel):
    email:str 
    password:str

class TokenData(BaseModel):
    email:str = None

class NewShipment(BaseModel):
    Invoice_no: int
    container_no: int
    shipment_description: str
    route_details:str
    goods_type: str
    device: str  
    expected_delivery_date: str
    PO_number: str
    delivery_no: int
    NDC_no: int
    batch_id: int
    Serial_no_of_goods: int

