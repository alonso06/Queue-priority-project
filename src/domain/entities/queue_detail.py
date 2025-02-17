import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class QueueDetail:
    id: uuid.UUID
    queue_id: uuid.UUID
    customer_id: uuid.UUID
    created_date: datetime
    updated_date: datetime | None = None