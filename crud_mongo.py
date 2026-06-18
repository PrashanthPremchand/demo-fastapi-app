from models_mongo import User

def create_user(name: str, email: str):
    user = User(name=name, email=email)
    user.save()
    return user

def get_users():
    return User.objects()

def get_user_by_id(user_id: str):
    return User.objects(id=user_id).first()

def update_user(user_id: str, name: str):
    user = User.objects(id=user_id).first()
    if user:
        user.name = name
        user.save()
    return user

def delete_user(user_id: str):
    user = User.objects(id=user_id).first()
    if user:
        user.delete()
    return user

