from sqlmodel import Session
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Queue


class QueueRepository( BaseRepository[Queue] ):
    def __init__(self, db: Session):
        super().__init__(db, Queue)