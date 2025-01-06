from dataclasses import dataclass


@dataclass
class QueuePriority:
    queue_id: str
    priority_id: str