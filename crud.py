from fastapi import FastAPI,status
from typing import Optional
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
app = FastAPI()
books = [
{
    "id": 1, 
    "title" : "The Romans"
}, 
{ 
    "id": 2, 
    "title": "New Man",
}
]
@app.get("/") 
def greet(): 
    return "Hey Welcome User"
# Read the databse 
@app.get("/book") 
def get_book(): 
    return books 
class Books(BaseModel): 
    id:int 
    title:str
#Create/ADD records to the databse
@app.post("/book")
def create_book(obj:Books):
    new_obj = obj.model_dump()
    books.append(new_obj) 
    return books
@app.get("/book/{book_id}")
#Retrieve Particular Records 
def get_id(book_id:int):   
    for i in books: 
        if(i['id']==book_id): 
            return"Book id exsits" ,i
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="No there bro !")
#Update a exsisting record 
class Book_Update(BaseModel): 
    title:str
@app.put("/book/{book_id}")
def update_book(obj:Book_Update,book_id:int): 
    for book in books: 
         if(book['id']==book_id):
             book['title'] = obj.title
             return book 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Book not present") 
             
#Delete records 
@app.delete("/book/{book_id}")
def delete_book(book_id:int) :
    for book in books: 
        if(book['id']==book_id): 
            books.remove(book) 
            return "Book with Book id ",book_id," Has been Removed !"
        return books 
    raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail="Book is already not present")
