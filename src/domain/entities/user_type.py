from dataclasses import dataclass

@dataclass
class UserType():
    name: str
    state: bool = True