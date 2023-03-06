from fastapi import HTTPException
from user import User
import re

def validation(user:User):
 input_pass =user.password
 pass_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"# compiling regex
 comp = re.compile(pass_regex)
 sear = re.search(comp, input_pass)
 
 
 
 email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
 input_email =user.email

 email_valid =re.fullmatch(email_regex, input_email)

 if len(user.username)==0:
  raise HTTPException(
        status_code=400,detail= "username is not empty"
     )
 elif len(user.username)>10:
  raise HTTPException(
        status_code=400,detail= "username is not exceed 16 characters"
     )

 if not sear:
  raise HTTPException(
        status_code=400,detail= "Password must follow pattern"
     )
 
 elif not email_valid:
  raise HTTPException(
        status_code=400,detail= "email invalid!!"
     )
 
 
  


