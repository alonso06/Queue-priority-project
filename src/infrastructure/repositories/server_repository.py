from sqlmodel import Session
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Server


class ServerRepository( BaseRepository[Server] ):
    def __init__(self, db: Session):
        super().__init__(db, Server)