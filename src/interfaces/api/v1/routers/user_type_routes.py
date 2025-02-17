from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.database import get_session
from src.interfaces.api.v1.schemas.user_type_schema import ViewUserType 
from src.application.use_cases import UserTypeUseCase  
from src.infrastructure.repositories import UserTypeRepository

router = APIRouter()

@router.get("/list", 
            response_model=list[ViewUserType])
def get_user_types(db:Session=Depends(get_session)):
    user_t_repo = UserTypeRepository(db=db)
    user_t_use_case = UserTypeUseCase(
                user_type_repository=user_t_repo) 
    return user_t_use_case.list()

@router.get("/get_user_type/{id}", 
            response_model=ViewUserType)
def get_user_type(id:str, db:Session=Depends(get_session)):
    user_t_repo = UserTypeRepository(db=db)
    user_t_use_case = UserTypeUseCase(
                user_type_repository=user_t_repo) 
    return user_t_use_case.get_by_id(id=id)