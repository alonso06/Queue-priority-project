from sqlmodel import Session
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Customer


class CustomerRepository( BaseRepository[Customer] ):
    def __init__(self, db: Session):
        super().__init__(db, Customer)