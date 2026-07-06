from sqlalchemy import create_engine #create engine is used to create connection to database 
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
load_dotenv()
import os 
#Creating a connection
print(os.getenv("MYSQL_URL"))
engine = create_engine(os.getenv("MYSQL_URL"))

#session 
session_local = sessionmaker(autoflush=False,autocommit =False,bind = engine)

def get_db() :
    db = session_local()
    try:
       yield db
    finally:
        db.close()
        
#Base 
 
base = declarative_base()