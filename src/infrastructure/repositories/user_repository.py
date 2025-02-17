from sqlmodel import Session
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import User as UserModel
from src.interfaces.api.v1.schemas import ViewUser
from src.domain.entities import User


class UserRepository( BaseRepository[UserModel, ViewUser, User] ):
    def __init__(self, db: Session):
        super().__init__(db, UserModel, ViewUser, User)