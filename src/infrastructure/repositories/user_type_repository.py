from sqlmodel import Session
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import UserType as UserTypeModel
from src.interfaces.api.v1.schemas import ViewUserType
from src.domain.entities import UserType


class UserTypeRepository( BaseRepository[UserTypeModel, 
                        ViewUserType, 
                        UserType] ):
    def __init__(self, db: Session):
        super().__init__(db, 
                         UserTypeModel,
                         ViewUserType, 
                         UserType)