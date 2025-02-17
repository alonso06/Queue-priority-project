import uuid

from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infrastructure.models import UserType, Server

class User(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, 
        primary_key=True)
    user_name: str = Field(max_length=12)
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=180)
    state: bool = Field(default=True)
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    user_type_id: uuid.UUID = Field(foreign_key="usertype.id")
    
    user_types: "UserType" = Relationship(
        back_populates="users"
    )
    servers: list["Server"] = Relationship(
        back_populates="users"
    )
