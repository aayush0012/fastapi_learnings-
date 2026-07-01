from fastapi import FastAPI,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel
app=FastAPI()
class Bookstore(BaseModel): 
    id:int
    title:str
    author:str
@app.post("/book")
def create_book(obj:Bookstore,db: Session=Depends(get_db)): 
    new_obj = model.Book(id=obj.id,title=obj.title,author=obj.author) 
    db.add(new_obj)
    db.commit() 
    db.refresh(new_obj)
    return new_obj 
@app.get("/book")
def get_id(db:Session=Depends(get_db)): 
    ans = db.query(model.Book).all()
    return ans