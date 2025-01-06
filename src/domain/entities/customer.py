from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    priority_id: str
    order_number: Optional[str] = None
    