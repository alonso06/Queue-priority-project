import uuid
from datetime import datetime
from dataclasses import dataclass

@dataclass
class User():
    id: uuid.UUID
    user_name: str
    first_name: str
    last_name: str
    state: bool
    user_type_id: uuid.UUID
    created_date: datetime
    updated_date: datetime | None = None