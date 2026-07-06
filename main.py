from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import models,schemas,utils 
from auth_database import get_db
from jose import jwt 
import os  
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from utils import hash_password,verify_password
from fastapi.security import OAuth2PasswordRequestForm
from auth_database import engine, base
base.metadata.create_all(bind=engine)
load_dotenv()
secret_key  = os.getenv("SECRET_KEY") # Secret key import kra li env file se
algo = os.getenv("ALGORITHM") # Algorithm jo use kreenge voh bhi impor kra li
expire_time  = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data:dict): 
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes =expire_time)
    to_encode.update({'exp': expire}) # dict me ek new key add krdi name exp 
    encode_jwt = jwt.encode(to_encode, secret_key, algorithm=algo)
    return encode_jwt

app = FastAPI()
@app.post("/signup")
# user:schemas.Usercreate  yaani user me saara response body store hogya and it should follow the structure of UserCreate table schema 
def register_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    exsisting_user = db.query(models.User).filter(models.User.username == user.username).first()
    if exsisting_user: 
        raise HTTPException(status_code=400,detail ="User already exsits")
    hashed_pass = hash_password(user.password)
    # We now want to add this entry to the database
    new_user = models.User(
        username = user.username, 
        email=user.email,
        hashed_password = hashed_pass, 
        role=user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

@app.post("/login")
def log_user(user:schemas.UserLogin,db:Session=Depends(get_db)):
    # If the user says itss logged in then it we can verify its record in the model.user table 
    exsisting_user = db.query(models.User).filter(models.User.username==user.username).first() 
    if(exsisting_user is None): 
        raise HTTPException(status_code=400, detail="User has not signed in !")
    if(verify_password(user.password,exsisting_user.hashed_password)): 
        token_data = {
        "sub": exsisting_user.username,
        "role": exsisting_user.role
}
        token = create_access_token(token_data)
        return  {"token :":token, "token_type :":"bearer"}
    else :
        raise HTTPException(status_code=400,detail="User Cred wrong!")
    
     