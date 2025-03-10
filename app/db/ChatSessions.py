from pydantic import BaseModel
from .DataBase import fake_db_sessions
import uuid

class Session(BaseModel):
    id: str
    name: str

def new_session(name: str):
    new = Session(id=str(uuid.uuid4()), name=name)
    fake_db_sessions.append(new)
    return new_session



fake_db_sessions.append(new_session("main chat"))
fake_db_sessions.append(new_session("third chat"))