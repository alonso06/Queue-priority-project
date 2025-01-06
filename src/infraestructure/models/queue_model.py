import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infraestructure.models import ServerQueue, QueueDetail, QueuePriority

class Queue(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    size: int
    state: bool = Field(default=True)
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    
    server_queues: list["ServerQueue"] = Relationship(
        back_populates="queues"
    )
    queue_detail: list["QueueDetail"] = Relationship(
        back_populates="queues"
    )
    queue_priorities: list["QueuePriority"] = Relationship(
        back_populates="queues"
    )