from fastapi import APIRouter
from src.interfaces.api.v1.routers import UserTypeRouter


api = APIRouter()

api.include_router(
    router=UserTypeRouter,
    prefix="/user_type"
)