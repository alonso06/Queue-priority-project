import os

from dotenv import load_dotenv
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.infraestructure.models import *

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    PROJECT_NAME: str = f"Queue_API - {os.getenv('ENV')}"
    DESCRIPTION: str = "Queue manager developed with FastAPI"
    ENV: Literal["development", "staging", "production"] = "development"
    VERSION: str = "0.1"
    DATABASE_URI: str = f"postgresql+psycopg2://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    API_USERNAME: str = "ach_test"
    API_PASSWORD: str = "ach_test_psw"
    
settings = Settings()
