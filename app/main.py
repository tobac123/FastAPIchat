from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi import websockets, FastAPI
import fastapi


app = FastAPI()

templates = Jinja2Templates(directory="HTML")

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/session", response_class=HTMLResponse)
async def sessions(request: Request):
    return templates.TemplateResponse(request=request, name="session.html")

@app.post("/session")
async def logindata(request: Request):
    pass # continue here