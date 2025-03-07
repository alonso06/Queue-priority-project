from typing import Sequence
from src.infrastructure.repositories import UserTypeRepository
from src.domain.entities import UserType
from src.infrastructure.models import (
    UserType as UserTypeModel)
from src.interfaces.api.v1.schemas import (
    UserTypeCreate, UserTypeUpdate)


class UserTypeUseCase:
    def __init__(self, user_type_repository:UserTypeRepository ):
        self.user_type_repository = user_type_repository
        
    def list(self) -> Sequence[UserType]:
        return self.user_type_repository.list()
    
    def get_by_id(self, id) -> UserType:
        return self.user_type_repository.get_by_id(id=id)
    
    def create(self, 
               obj_user_t_sch:UserTypeCreate) -> UserType:
        
        obj_user_t_model = UserTypeModel.model_validate(
                        obj_user_t_sch.model_dump())
        return self.user_type_repository.create(
                obj_data=obj_user_t_model)
        
    def update(self,
               id:str,
               obj_user_t_sch:UserTypeUpdate) -> UserType:
        
        obj_user_t_model = UserTypeModel.model_validate(
                        obj_user_t_sch.model_dump())
        return self.user_type_repository.update(
                id=id,
                updated_data=obj_user_t_model)
        
    def unsubscribe(self, 
                    id:str):
        return self.user_type_repository.unsubscribe(id=id)
    
    def delete(self, 
                    id:str) -> dict[str,bool]:
        return self.user_type_repository.delete(id=id)