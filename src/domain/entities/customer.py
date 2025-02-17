import uuid
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Customer:
    id: uuid.UUID
    priority_id: uuid.UUID
    order_number: str | None
    created_date: datetime
    updated_date: datetime | None = None
    