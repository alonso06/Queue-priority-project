from sqlmodel import Session
from src.domain.entities import Queue
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Queue as QueueModel
from src.interfaces.api.v1.schemas import ViewQueue


class QueueRepository( BaseRepository[QueueModel,
                                      ViewQueue,
                                      Queue] ):
    def __init__(self, db: Session):
        super().__init__(db, 
                         QueueModel,
                         ViewQueue,
                         Queue)