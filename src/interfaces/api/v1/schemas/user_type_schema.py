import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


# TODO: agregar validación segun error
class ViewUserType(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    name: str 
    state: bool 
    created_date: datetime
    updated_date: datetime | None = Field(default=None)
        
class UserTypeCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)  
    name: str
    state: bool = Field(default=True)
    
class UserTypeUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str | None
    state: bool | None
    updated_date: datetime | None = Field(default=datetime.now())