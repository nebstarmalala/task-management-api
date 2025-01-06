from fastapi import APIRouter, Depends, HTTPException, status

userrouter = APIRouter()

@userrouter.get("/")
def list_users():
    return {"message": "user"}

@userrouter.post("/")
def create_user():
    return {"message": "user"}

@userrouter.get("/{user_id}/")
def get_user():
    return {"message": "user"}

@userrouter.put("/")
def update_user():
    return {"message": "user"}

@userrouter.delete("/")
def delete_user():
    return {"message": "user"}