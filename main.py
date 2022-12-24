from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app=FastAPI()





templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str,newdb:newdb):
   
    return templates.TemplateResponse("item.html", {"request": request, "id": id,"newdb":newdb})