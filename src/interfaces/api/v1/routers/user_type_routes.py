from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.database import get_session
from src.interfaces.api.v1.schemas import (
    ViewUserType,
    UserTypeCreate,
    UserTypeUpdate   
    )
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

@router.post("",
             response_model=ViewUserType)
def create_user_type(user_type:UserTypeCreate,
                     db:Session=Depends(get_session)):
    
    user_t_repo = UserTypeRepository(db=db)
    user_t_use_case = UserTypeUseCase(
            user_type_repository=user_t_repo)
    return user_t_use_case.create(
        obj_user_t_sch=user_type)
    
@router.put("/{id}")
def update_user_type(id:str,
                    user_type:UserTypeUpdate,
                    db:Session=Depends(get_session)):
    
    user_t_repo = UserTypeRepository(db=db)
    user_t_use_case = UserTypeUseCase(
            user_type_repository=user_t_repo)
    return user_t_use_case.update(
        id=id,
        obj_user_t_sch=user_type)
    
@router.patch("unsubscribe/{id}")
def unsubscribe_user_type(id:str,
                    db:Session=Depends(get_session)):
    
    user_t_repo = UserTypeRepository(db=db)
    user_t_use_case = UserTypeUseCase(
            user_type_repository=user_t_repo)
    return user_t_use_case.unsubscribe(id=id)

@router.delete("/{id}")
def delete_user_type(id:str,
                    db:Session=Depends(get_session)):
    
    user_t_repo = UserTypeRepository(db=db)
    user_t_use_case = UserTypeUseCase(
            user_type_repository=user_t_repo)
    return user_t_use_case.delete(id=id)