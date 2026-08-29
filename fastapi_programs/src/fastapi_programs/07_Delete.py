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


@app.put("/content/{content_id}")
def update_content(content_id:int, updated_content:contentCreate):
    for index, content in enumerate(contents):
        if content.id == content_id:
            updated_content_data = Content(id=content_id, **updated_content.model_dump())
            contents[index] = updated_content_data
            return{
                "message":"Content updated successfully",
                "data":updated_content_data
            }
    return{
        "message":"Resource not found"
    }


@app.delete("/content/{content_id}")
def delete_content(content_id:int):
    for index, content in enumerate(contents):
        if content.id == content_id:
            deleted_content = contents.pop(index)
            return{
                "message":"Content deleted successfully",
                "data":deleted_content
            }
    return{
        "message":"Resource not found"
    }