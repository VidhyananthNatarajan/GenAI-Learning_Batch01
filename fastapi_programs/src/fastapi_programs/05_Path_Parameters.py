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

@app.get("/all_contents")
def get_all_contents():
        return{
            "data":contents
        }

@app.get("/content/{content_id}")
def get_content_by_id(content_id:int):
    for content in contents:
        if content.id == content_id:
            return{
                "data":content
            }
    return{
        "message":"Content not found"
    }
