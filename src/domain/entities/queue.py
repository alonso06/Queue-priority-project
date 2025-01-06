from dataclasses import dataclass


@dataclass
class Queue:
    size: int
    state: bool
    