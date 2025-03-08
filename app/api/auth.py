fake_db = {
    "dwa": {"password": "dwa"},
    "user2": {"password": "dwa"}
}


def auth_user(username, password) -> bool:
    if username in fake_db and fake_db[username]["password"] == password:
        # Redirect to /session if valid
        return True
    else:
        return False