import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Queue:
    id: uuid.UUID
    name: str
    created_date: datetime
    size: int | None = None
    state: bool = True
    updated_date: datetime | None = None
    