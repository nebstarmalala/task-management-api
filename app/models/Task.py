from app.db.database_connection import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy import Uuid
import uuid
from datetime import datetime, date, time

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Uuid, primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String(255))
    description = Column(String(255))
    completed = Column(Boolean, default=False)
    user = Column(Uuid, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)