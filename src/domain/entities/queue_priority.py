import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class QueuePriority:
    id: uuid.UUID
    queue_id: uuid.UUID
    priority_id: uuid.UUID
    created_date: datetime
    updated_date: datetime | None = None