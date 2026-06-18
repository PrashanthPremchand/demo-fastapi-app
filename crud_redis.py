from redis import r

def set_user(name: str):
    r.set("user", name)
    return True

def get_user():
    value = r.get("user")
    return value.decode() if value else None

def delete_user():
    r.delete("user")
    return True