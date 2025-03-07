from sqlmodel import Session
from src.domain.entities import Priority
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Priority as PriorityModel
from src.interfaces.api.v1.schemas import ViewPriority


class PriorityRepository( BaseRepository[PriorityModel,
                                         ViewPriority,
                                         Priority] ):
    def __init__(self, db: Session):
        super().__init__(db, 
                         PriorityModel,
                         ViewPriority,
                         Priority)