import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Server:
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    description: str
    created_date: datetime
    updated_date: datetime | None = None