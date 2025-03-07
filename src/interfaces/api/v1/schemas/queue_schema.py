import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewQueue(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    name: str
    state: bool
    user_id: uuid.UUID | None = Field(default=None)
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    

class QueueCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str
    state: bool
    user_id: uuid.UUID

class QueueUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str | None
    state: bool | None
    user_id: uuid.UUID | None
    updated_date: datetime | None = Field(default=datetime.now())