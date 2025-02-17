import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewServer(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    description: str 
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    
    class Config:
        orm_mode= True
    

class ServerCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: uuid.UUID
    name: str 
    description: str
    
class ServerUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: uuid.UUID | None
    name: str | None
    description: str | None
    
