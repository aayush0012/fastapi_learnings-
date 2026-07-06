from pydantic import BaseModel,EmailStr
# defining all the tables syntax that we are constructing 
class UserCreate(BaseModel): 
    username:str
    email:str
    password:str
    role:str
class UserLogin(BaseModel):
    username:str
    password:str
    
