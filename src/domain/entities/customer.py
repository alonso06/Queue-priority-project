import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    id: uuid.UUID
    priority_id: uuid.UUID
    created_date: datetime
    dni: str | None = None
    state: bool = True
    updated_date: datetime | None = None
    