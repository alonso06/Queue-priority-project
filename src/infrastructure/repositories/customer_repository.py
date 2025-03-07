from sqlmodel import Session
from src.domain.entities import Customer
from src.infrastructure.repositories import BaseRepository
from src.infrastructure.models import Customer as CustomerModel
from src.interfaces.api.v1.schemas import ViewCustomer


class CustomerRepository( BaseRepository[CustomerModel,
                                         ViewCustomer,
                                         Customer] ):
    def __init__(self, db: Session):
        super().__init__(db, CustomerModel,
                         ViewCustomer,
                         Customer)