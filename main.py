from fastapi import FastAPI, Depends, HTTPException, status
# from db import get_connection
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models
import schemas
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model= list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/user/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.put("/user/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)

@app.delete("/user/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)

from mongoengine import connect
from schemas_mongo import UserCreate, UserResponse
import crud_mongo
import os
from dotenv import load_dotenv

load_dotenv()

connect(host=os.getenv("MONGO_URL"))

@app.post("/mongo/users", response_model=UserResponse)
def creat_user(user: UserCreate):
    user = crud_mongo.create_user(user.name, user.email)
    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email
    )

@app.get("/mongo/users", response_model=list[UserResponse])
def get_users():
    users = crud_mongo.get_users()
    return [
        UserResponse(
            id=str(u.id),
            name=u.name,
            email=u.email
        )
        for u in users
    ]

@app.get("/mongo/user/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    user = crud_mongo.get_user_by_id(user_id)
    if not user:
        return {
            "message": "User not found"
        }
    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email
    )

@app.put("/mongo/{user_id}", response_model=UserResponse)
def update_user(user_id: str, name: str):
    user = crud_mongo.update_user(user_id, name)
    if not user:
        return {
            "message": "User not found"
        }
    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email
    )

@app.delete("/mongo/{user_id}", response_model=UserResponse)
def delete_user(user_id: str):
    user = crud_mongo.delete_user(user_id)
    if not user:
        return {
            "message": "User not found"
        }
    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email
    )


from schemas_redis import UserRedis, UserRedisResponse
import crud_redis

@app.post("/redis/user", response_model=UserRedisResponse)
def set_user(user: UserRedis):
    crud_redis.set_user(user)
    return {
        "meassage": "Saved"
    }

@app.get("/redis/user", response_model=UserRedisResponse)
def get_user():
    value = crud_redis.get_user()
    return {
        "user": value
    }

@app.delete("/redis/user", response_model=UserRedisResponse)
def delete_user():
    crud_redis.delete_user()
    return {
        "message": "Deleted"
    }


# @app.get("/")
# def read_root():
#     return {  
#         "Message": "Hello"
#     }

# @app.get("/user/{id}")
# def get_user(id: int, name: str = "guest"):
#     return {
#         "id" : id,
#         "name": name
#     }

# @app.get("/search")
# def search(name: str):
#     return {
#         "name" : name
#     }

# @app.get("/items/{item_id}")
# def get_item(item_id: int, price: float):
#     return {
#         "item id": item_id,
#         "price": price
#     }

# @app.post("/users")
# def create_user(name: str, email: str):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#     values = (name, email)

#     cursor.execute(query, values)
#     conn.commit()

#     cursor.close()
#     conn.close()

#     return {
#         "message": "user created",
#         "name": name,
#         "email": email
#     }

# @app.get("/users")
# def get_users():
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = "SELECT * FROM users"

#     cursor.execute(query)
#     result = cursor.fetchall()

#     users = []
#     for currentUser in result:
#         users.append({
#             "id": currentUser[0],
#             "name": currentUser[1],
#             "email": currentUser[2]
#         })
    
#     cursor.close()
#     conn.close()

#     return {"data": users}

# @app.get("/users/{id}")
# def get_user(id: int):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = "SELECT * FROM users WHERE id=%s"

#     cursor.execute(query, (id,))
#     user = cursor.fetchone()

#     cursor.close()
#     conn.close()

#     if user:
#         return {
#             "id": user[0],
#             "name": user[1],
#             "eamil": user[2]
#         }
        
#     return {"message": "User not found"}

# @app.put("/user/{id}")
# def update_user(id: int, name: str, email: str):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
#     values = (name, email, id)

#     cursor.execute(query, values)
#     conn.commit()

#     cursor.close()
#     conn.close()

#     return {
#         "message": "User updated",
#         "name": name,
#         "email": email
#         }

# @app.delete("/user/{id}")
# def delete_user(id: int):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = "DELETE FROM users WHERE id=%s"

#     cursor.execute(query, (id,))
#     conn.commit()

#     cursor.close()
#     conn.close()

#     return {"message": "user deleted"}
