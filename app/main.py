from fastapi import FastAPI
from api import routes
from api.WebSocket import ws_router


app = FastAPI()
app.include_router(routes.router)
app.include_router(ws_router)

