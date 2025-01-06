from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, Optional
from app.db.database_connection import SessionLocal, get_db
from app.models.User import User
from app.schema.user_schema import UserInCreate, UserInResponse

userrouter = APIRouter()
db_dependency = Annotated[SessionLocal, Depends(get_db)]

@userrouter.get("/", status_code=status.HTTP_200_OK)
async def list_users(db: db_dependency): # type: ignore
    users = db.query(User).all()
    return users

@userrouter.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserInCreate, db: db_dependency) -> UserInResponse: # type: ignore
    user = User(name=user.name, email=user.email, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@userrouter.get("/{user_id}/", status_code=status.HTTP_200_OK)
def get_user():
    return {"message": "user"}

@userrouter.put("/", status_code=status.HTTP_200_OK)
def update_user():
    return {"message": "user"}

@userrouter.delete("/", status_code=status.HTTP_200_OK)
def delete_user():
    return {"message": "user"}