from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates = Jinja2Templates(directory="templates")

fackdb=[
    {
        "id":1,"name":"smasung m21","price":120
    },
    {
        "id":2,"name":"smasung m31","price":121
    },
    {
        "id":3,"name":"smasung m51","price":123
    },

]
@app.get('/',response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):  
    return templates.TemplateResponse("item.html", {"request": request, "id": id,})
