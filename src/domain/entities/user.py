from dataclasses import dataclass
from datetime import datetime

@dataclass
class User():
    user_type_id: str
    first_name: str
    last_name: str
    birthdate: datetime
    state: bool = True
    
