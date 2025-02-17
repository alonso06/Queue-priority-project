import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewQueuePriority(BaseModel):
    id: uuid.UUID
    queue_id: uuid.UUID
    priority_id: uuid.UUID
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    
    class Config:
        orm_mode= True
    
class QueuePriorityCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    queue_id: uuid.UUID
    priority_id: uuid.UUID

class QueuePriorityUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    queue_id: uuid.UUID
    priority_id: uuid.UUID