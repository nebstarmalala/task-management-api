from pydantic import EmailStr, BaseModel
from typing import Union
from uuid import UUID 
from datetime import datetime

class UserInCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

class UserInResponse(BaseModel):
    id: UUID
    name: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

class UserInUpdate(BaseModel):
    id: UUID
    username: Union[str, None] = None
    name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None

class UserInLogin(BaseModel):
    username: str
    password: str

class UserWithToken(BaseModel):
    access_token: str
    token_type: str