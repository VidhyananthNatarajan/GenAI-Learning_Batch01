from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class contentCreate(BaseModel):
    title: str
    description: str
    author: str
    views:int

class Content(contentCreate):
    id:int    

contents =[]

next_id=1

@app.post("/create_content")
def create_content(content:contentCreate):
    global next_id
    new_content = Content(id = next_id, **content.model_dump())
    contents.append(new_content)
    next_id +=1
    return{
       "message":"Content created successfully",
       "data":new_content
       
    }