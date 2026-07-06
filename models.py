from sqlalchemy import Column,Integer,String
from auth_database import base 
#here we make the table 
class User(base):
    __tablename__ = "User"
    id = Column(Integer,primary_key=True,index=True)
    username= Column(String(255),unique=True,index=True)
    email=  Column(String(255),unique=True,index=True)
    hashed_password=  Column(String(255))
    role=  Column(String(255),default="user")