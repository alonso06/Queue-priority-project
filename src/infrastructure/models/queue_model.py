import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.infrastructure.models import (User, 
                                           QueueDetail, 
                                           QueuePriority)

class Queue(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    name: str = Field(max_length=20)
    state: bool = Field(default=True)
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    user_id: uuid.UUID | None = Field(default=None, 
                                      unique=True, 
                                      foreign_key="user.id")
    user: Optional["User"] = Relationship(
        back_populates="queue"
    ) 
    queue_detail: list["QueueDetail"] = Relationship(
        back_populates="queues"
    )
    queue_priorities: list["QueuePriority"] = Relationship(
        back_populates="queues"
    )