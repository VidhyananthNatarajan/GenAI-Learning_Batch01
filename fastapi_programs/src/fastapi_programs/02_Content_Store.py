from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class content(BaseModel):
    title: str
    description: str
    author: str
    views:int

contents =[]

@app.post("/create_content")
def create_content(content:content):
    contents.append(content)
    return{
       "message":"Content created successfully",
       "data":content
       
    }