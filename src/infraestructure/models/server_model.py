import uuid

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy import Column
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infraestructure.models import User, ServerQueue

class Server(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True
    )
    description: str = Field(sa_column=Column(TEXT))
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    
    users: "User" = Relationship(
        back_populates="servers"
    )
    server_queues: list["ServerQueue"] = Relationship(
        back_populates="servers"
    )