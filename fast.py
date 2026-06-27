from fastapi import FastAPI
from typing import Optional 
app = FastAPI()
@app.get("/")
def read_root():
    return {"Message":"Hell"}
@app.get("/greet")
def greet(name:str,age:Optional[int]=12): 
    return {"Message":f"Hello, welcome to FastAPI! {name}", "Age": age}