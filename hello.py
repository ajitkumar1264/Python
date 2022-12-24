from tokenize import String
from fastapi import FastAPI
from typing import Optional, Union
from pydantic import BaseModel

app=FastAPI()

Fackedb=[]

class course(BaseModel):
  id:int
  name:str
  price:float


@app.get("/")
def read():
    return{"hello":"Hello  fast api"}



@app.get("/course")
def get_course():
    return Fackedb

@app.get("/course/{id}")
def get_course1(id: int):
    course=id-1
    return Fackedb[course]

@app.post("/course")
def add_course(course:course):
  Fackedb.append(course.dict())
  return Fackedb[-1]

@app.delete("/course/{id}")
def del_course(course:int):
    Fackedb.pop(course-1)
    return {"task":"succesfully completed"}


