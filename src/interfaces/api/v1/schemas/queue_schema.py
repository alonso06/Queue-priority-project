import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewQueue(BaseModel):
    id: uuid.UUID
    size: int | None
    name: str
    state: bool
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    
    class Config:
        orm_mode= True
    
class QueueCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    size: int | None = Field(default=None)
    name: str
    state: bool

class QueueUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    size: int | None
    name: str | None
    state: bool | None