import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infrastructure.models import Queue, Priority

class QueuePriority(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    queue_id: uuid.UUID = Field(foreign_key="queue.id")
    priority_id: uuid.UUID = Field(foreign_key="priority.id")
    
    queues: "Queue" = Relationship(
        back_populates="queue_priorities"
    )
    priorities: "Priority" = Relationship(
        back_populates="queue_priorities"
    )