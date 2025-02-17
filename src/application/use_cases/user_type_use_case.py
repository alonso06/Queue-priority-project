from typing import Sequence
from src.infrastructure.repositories import UserTypeRepository
from src.domain.entities import UserType


class UserTypeUseCase:
    def __init__(self, user_type_repository:UserTypeRepository ):
        self.user_type_repository = user_type_repository
        
    def list(self) -> Sequence[UserType]:
        return self.user_type_repository.list()
    
    def get_by_id(self, id) -> UserType:
        return self.user_type_repository.get_by_id(id=id)
        