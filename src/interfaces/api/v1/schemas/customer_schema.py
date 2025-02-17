import uuid
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ViewCustomer(BaseModel):
    id: uuid.UUID
    priority_id: uuid.UUID
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
    order_number: str | None
    
    class Config:
        orm_mode= True
    
class CustomerCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    priority_id: uuid.UUID
    order_number: str | None

class CustomerUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    priority_id: uuid.UUID | None
    order_number: str | None