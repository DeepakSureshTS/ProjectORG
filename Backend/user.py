from pydantic import BaseModel, Field

password_regex= "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"
email_regex="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
class User(BaseModel):
    username:str = Field(min_length=4,max_length=32)
    email:str = Field(...,regex= email_regex)
    password:str = Field(...,regex=password_regex)

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

