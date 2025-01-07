from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, Optional, List
from app.db.database_connection import SessionLocal, get_db
from app.models.Task import Task
from app.schema.task_schema import TaskInCreate, TaskInResponse, TaskInUpdate
from uuid import UUID

taskrouter = APIRouter()
db_dependency = Annotated[SessionLocal, Depends(get_db)]

@taskrouter.get("/", status_code=status.HTTP_200_OK)
async def list_tasks(db: db_dependency) -> List[TaskInResponse]: # type: ignore
    tasks = db.query(Task).all()
    return tasks

@taskrouter.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskInCreate, db: db_dependency) -> TaskInResponse: # type: ignore
    task = Task(title=task.title, description=task.description, completed=task.completed, user=task.user)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@taskrouter.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: UUID, db: db_dependency) -> TaskInResponse: # type: ignore
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@taskrouter.put("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: UUID, task: TaskInUpdate, db: db_dependency) -> TaskInResponse: # type: ignore
    task_db = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    task_db.title = task.title
    task_db.description = task.description
    task_db.completed = task.completed
    task_db.user = task.user
    db.commit()
    db.refresh(task_db)
    return task_db

@taskrouter.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: UUID, db: db_dependency): # type: ignore
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.delete(task)
    db.commit()
    return