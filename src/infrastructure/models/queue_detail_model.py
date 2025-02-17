import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infrastructure.models import Queue, Customer

class QueueDetail(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    
    queue_id: uuid.UUID = Field(foreign_key="queue.id")
    customer_id: int = Field(foreign_key="customer.id")
    queues: "Queue" = Relationship(
        back_populates="queue_detail"
    )
    customers: "Customer" = Relationship(
        back_populates="queue_detail"
    )
    
    