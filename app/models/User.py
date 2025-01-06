from app.db.database_connection import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy import Uuid
import uuid
from datetime import datetime, date, time

class User(Base):
    __tablename__ = "users"
    
    id = Column(Uuid, primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)