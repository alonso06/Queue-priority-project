import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewUser(BaseModel):
    id: uuid.UUID
    user_name: str 
    first_name: str 
    last_name: int 
    state: bool 
    user_type_id: uuid.UUID 
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    
    class Config:
        orm_mode= True
    

class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_type_id: str
    first_name: str
    last_name: str
    state: bool = Field(default=True)
    
class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_type_id: str | None
    first_name: str | None
    last_name: str | None
    state: bool | None
    
