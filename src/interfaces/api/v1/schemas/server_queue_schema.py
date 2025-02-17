import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewQueueDetail(BaseModel):
    id: uuid.UUID
    queue_id: uuid.UUID
    server_id: uuid.UUID
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    
    class Config:
        orm_mode= True
    
class QueueDetailCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    queue_id: uuid.UUID
    server_id: uuid.UUID


class QueueDetailUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    queue_id: uuid.UUID | None
    server_id: uuid.UUID | None
