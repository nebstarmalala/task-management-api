from app.db.database_connection import Base, engine
from app.models.User import User

def create_tables():
    Base.metadata.create_all(bind=engine)