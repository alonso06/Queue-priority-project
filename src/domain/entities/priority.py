import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Priority:
    id: uuid.UUID
    name: str
    description: str
    created_date: datetime
    state: bool=True
    updated_date: datetime | None = None  