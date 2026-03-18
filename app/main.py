from fastapi import FastAPI
from app.api import routes
from app.api import WebSocket


app = FastAPI()
app.include_router(routes.router)
app.include_router(WebSocket.ws_router)

