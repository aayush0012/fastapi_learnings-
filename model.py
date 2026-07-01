from database import base 
from sqlalchemy import Column,Integer,VARCHAR 
class Book(base): 
    __tablename__ ="books"
    id = Column(Integer,primary_key=True,index=True) 
    title=Column(VARCHAR(200))
    author =Column(VARCHAR(100)) 
    