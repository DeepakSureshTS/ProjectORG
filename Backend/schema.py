def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "username":str(item["username"]),
        "email":str(item["email"]),
        "password":str(item["password"]),
        "cpassword":str(item["cpassword"]),
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]