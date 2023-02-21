def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "username":str(item["username"]),
        "email":str(item["email"]),
        "password":str(item["password"]),
        # "cpassword":str(item["cpassword"]),
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def shipEntity(item) -> dict:
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

def shipsEntity(entity) -> list:
    return [shipEntity(item) for item in entity]