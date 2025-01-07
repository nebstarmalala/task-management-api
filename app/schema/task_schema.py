from pydantic import BaseModel
from typing import Union
from uuid import UUID
from datetime import datetime

class TaskInCreate(BaseModel):
    title: str
    description: str
    completed: bool
    user: UUID

class TaskInResponse(BaseModel):
    id: UUID
    title: str
    description: str
    completed: bool
    user: UUID
    created_at: datetime
    updated_at: datetime

class TaskInUpdate(BaseModel):
    id: UUID
    title: Union[str, None] = None
    description: Union[str, None] = None
    completed: Union[bool, None] = None
    user: Union[UUID, None] = None
