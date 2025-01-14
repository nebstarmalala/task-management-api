from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, Optional, List
from app.db.database_connection import SessionLocal, get_db
from app.models.User import User
from app.schema.user_schema import UserInCreate, UserInResponse, UserInUpdate
from uuid import UUID
from passlib.context import CryptContext
from app.routers.auth import get_current_user

userrouter = APIRouter()
db_dependency = Annotated[SessionLocal, Depends(get_db)]
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user_dependency = Annotated[User, Depends(get_current_user)]

@userrouter.get("/", status_code=status.HTTP_200_OK)
async def list_users(db: db_dependency) -> List[UserInResponse]: # type: ignore
    users = db.query(User).all()
    return users

@userrouter.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserInCreate, db: db_dependency) -> UserInResponse: # type: ignore
    user = User(name=user.name, username=user.username, email=user.email, password=pwd_context.hash(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@userrouter.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: UUID, db: db_dependency) -> UserInResponse: # type: ignore
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@userrouter.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: UUID, user: UserInUpdate, db: db_dependency) -> UserInResponse: # type: ignore
    user_db = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user_db.name = user.name
    user_db.username = user.username
    user_db.email = user.email
    user_db.password = pwd_context.hash(user.password)
    db.commit()
    db.refresh(user_db)
    return user_db


@userrouter.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: UUID, db: db_dependency): # type: ignore
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return