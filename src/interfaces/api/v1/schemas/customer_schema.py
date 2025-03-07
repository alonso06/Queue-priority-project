import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewCustomer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    
    dni: str | None = Field(default=None)
    state: bool = Field(default=True)
    created_date: datetime
    updated_date: datetime | None = Field(default=None)

class CustomerCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    dni: str | None = Field(default=None)

class CustomerUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    dni: str | None 
    state: bool | None