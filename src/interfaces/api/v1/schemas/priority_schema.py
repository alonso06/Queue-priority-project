import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewPriority(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    name: str
    description: str
    state: bool
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    
class PriorityCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    description: str
    state: bool = Field(default=True)

class PriorityUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str | None
    description: str | None
    state: bool | None