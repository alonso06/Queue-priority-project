from sqlmodel import Session
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Priority


class PriorityRepository( BaseRepository[Priority] ):
    def __init__(self, db: Session):
        super().__init__(db, Priority)