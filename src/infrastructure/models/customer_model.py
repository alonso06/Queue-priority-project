import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infrastructure.models import Priority, QueueDetail
class Customer(SQLModel, table=True):
    id: int | None = Field(
        default=None, 
        primary_key=True
    )
    dni: str | None = Field(nullable=True, max_length=8, 
                            unique=True)
    state: bool = Field(default=True)
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)   
    priority_id: uuid.UUID = Field(
        foreign_key="priority.id"
    )

    priorities: "Priority" = Relationship(
        back_populates="customers"
    )
    queue_detail: list["QueueDetail"] = Relationship(
        back_populates="customers"
    )