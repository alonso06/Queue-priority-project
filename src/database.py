from sqlmodel import Session, SQLModel, create_engine
from src.config import *



engine = create_engine(
    settings.DATABASE_URI, 
    echo=True
    
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def drop_db():
    SQLModel.metadata.drop_all(engine)

def get_session():
    with Session(engine) as session:
        yield session