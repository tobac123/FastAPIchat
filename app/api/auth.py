from app.db import fake_db_user


def auth_user(username, password) -> bool:
    if username in fake_db_user and fake_db_user[username]["password"] == password:
        return True
    else:
        return False