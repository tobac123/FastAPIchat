from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .auth import auth_user

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_post(username: str = Form(...), password: str = Form(...)):
    print(f"username: {username}; password: {password}")
    if auth_user(username, password):
        return RedirectResponse(url="/session", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/session", response_class=HTMLResponse)
async def session_page(request: Request):
    return templates.TemplateResponse("session.html", {"request": request})
