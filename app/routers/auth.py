from fastapi import APIRouter, Depends, HTTPException, status

authrouter = APIRouter()

@authrouter.post("/login")
def login():
    return {"message": "user"}

@authrouter.post("/register")
def register():
    return {"message": "user"}