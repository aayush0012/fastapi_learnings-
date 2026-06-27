from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel as base
app = FastAPI()
@app.get("/")
def read_root():
    return {"Message":"Hell"}
@app.get("/greet")
def greet(name:str,age:Optional[int]=12): 
    return {"Message":f"Hello, welcome to FastAPI! {name}", "Age": age}
class Student(base): 
    name:str
    age:int
    roll_no:int
@app.post("/create_student")
def create(student:Student):
        return{
            "Message": f"Student name is {student.name},age is {student.age}, and roll number is {student.roll_no}"
        }