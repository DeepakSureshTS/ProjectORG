from pydantic import BaseModel, Field
from mongoengine import Document, StringField, IntField, DateField
from datetime import datetime


password_regex= "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"
email_regex="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
class User(BaseModel):
    username:str = Field(min_length=4,max_length=32)
    email:str = Field(...,regex= email_regex)
    password:str = Field(...,regex=password_regex)
    cpassword:str

class Login(BaseModel):
    email:str
    password:str

class NewShipment(BaseModel):
    Invoice_no: int
    container_no: int
    shipment_description: str
    route_details: str
    goods_type: str
    device: str
    expected_delivery_date: datetime
    PO_number: str
    delivery_no: int
    NDC_no: int
    batch_id: int
    Serial_no_of_goods: int

class Shipments(Document):
    Invoice_no = IntField()
    container_no = IntField()
    shipment_description = StringField()
    route_details = StringField()
    goods_type = StringField()
    device = StringField()
    expected_delivery_date = DateField()
    PO_number = StringField()
    delivery_no = IntField()
    NDC_no = IntField()
    batch_id = IntField()
    Serial_no_of_goods = IntField()
    
 