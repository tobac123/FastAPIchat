from typing import List

from fastapi import APIRouter, Request, Form, HTTPException, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.db import Session, SessionCreate, fake_db_sessions, new_session
from .auth import auth_user

templates = Jinja2Templates(directory="templates")
router = APIRouter()

# LOGIN RUTES:

@router.get("/", response_class=HTMLResponse)
async def rout():
    return RedirectResponse("/login")

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

# SESSION RUTES:

@router.get("/sessions", response_model=List[Session])
async def get_sessions():
    """Return all chat sessions."""
    return fake_db_sessions

@router.post("/sessions", response_model=SessionCreate)
async def create_session(session: SessionCreate):
    """Create a new chat session and return it."""
    return new_session(session.name)

# CHAT RUTES:

@router.get("/chat.html")
async def chat(request: Request, session: str = Query(...)):
    return templates.TemplateResponse("chat.html", {"request": request, "session": session})