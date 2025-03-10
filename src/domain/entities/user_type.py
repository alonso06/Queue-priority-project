import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserType():
    id: uuid.UUID
    name: str
    created_date: datetime
    state: bool = True
    updated_date: datetime | None = None