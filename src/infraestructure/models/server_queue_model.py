import uuid

from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infraestructure.models import Queue, Server

class ServerQueue(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)  
    queue_id: uuid.UUID = Field(foreign_key="queue.id")
    server_id: uuid.UUID = Field(foreign_key="server.id")
    
    queues: "Queue" = Relationship(
        back_populates="server_queues"
    )
    servers: "Server" = Relationship(
        back_populates="server_queues"
    )