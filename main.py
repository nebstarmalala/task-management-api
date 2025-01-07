from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.init_database import create_tables
from app.routers.auth import authrouter
from app.routers.user import userrouter
from app.routers.task import taskrouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(authrouter, tags=["auth"], prefix="/auth")
app.include_router(userrouter, tags=["users"], prefix="/users")
app.include_router(taskrouter, tags=["tasks"], prefix="/tasks")

