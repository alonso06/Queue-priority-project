import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy import Column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infrastructure.models import QueuePriority, Customer

class Priority(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    name: str = Field(max_length=80)
    description: str = Field(sa_column=Column(TEXT))
    state: bool = Field(default=True)
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    
    customers: list["Customer"] = Relationship(
        back_populates="priorities"
    )
    queue_priorities: list["QueuePriority"] = Relationship(
        back_populates="priorities"
    )