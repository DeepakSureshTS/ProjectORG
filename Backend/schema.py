def user_Entity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "username":str(item["username"]),
        "email":str(item["email"]),
        "password":str(item["password"]),        
    }

def users_Entity(entity) -> list:
    return [user_Entity(item) for item in entity]

def ship_Entity(item) -> dict:
    return{
        "Invoice_no":str(item["_id"]),
        "container_no":str(item["container_no"]),
        "shipment_description":str(item["shipment_description"]),
        "route_details":str(item["route_details"]),
        "goods_type":str(item["goods_type"]),
        "device":str(item["device"]),
        "expected_delivery_date":str(item["expected_delivery_date"]),
        "PO_number":str(item["PO_number"]),
        "delivery_no":str(item["delivery_no"]),
        "NDC_no":str(item["NDC_no"]),
        "batch_id":str(item["batch_id"]),
        "Serial_no_of_goods":str(item["Serial_no_of_goods"]),
    }

def ships_Entity(entity) -> list:
    return [ship_Entity(item) for item in entity]

def login_Entity(item) -> dict:
    return{
        "email":str(item["email"]),
        "password":str(item["password"]),
    }

def logins_Entity(entity) -> list:
    return [login_Entity(item) for item in entity]

def device_Entity(item) -> dict:
    return{
        "Battery_Level":int(item["Battery_Level"]),
        "Device_Id":int(item["Device_Id"]),
        "First_Sensor_temperature":int(item["First_Sensor_temperature"]),
        "Route_From":str(item["Route_From"]),
        "Route_To":str(item["Route_To"]),
    }
def devices_Entity(entity) -> list:
    return [device_Entity(item) for item in entity]




