import uuid 

from typing import TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.infraestructure.models import User

class UserType(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, 
        primary_key=True)
    name: str = Field(max_length=50)
    state: bool = Field(default=True)
    created_date: datetime = Field(default=datetime.now)
    updated_date: datetime | None = Field(nullable=True)
    
    users: list["User"] = Relationship(back_populates="user_types")