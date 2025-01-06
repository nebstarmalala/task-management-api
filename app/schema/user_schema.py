from pydantic import EmailStr, BaseModel
from typing import Union
from uuid import UUID 

class UserInCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserInResponse(BaseModel):
    id: UUID
    name: str
    email: str
    created_at: str
    updated_at: str

class UserInUpdate(BaseModel):
    id: UUID
    name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None

class UserInLogin(BaseModel):
    email: EmailStr
    password: str

class UserWithToken(BaseModel):
    access_token: str
    token_type: str