from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config import Settings
from src.database import create_db_and_tables


# TODO:Agregar logger paquete loggin
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


# TODO: include_route
def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/docs",
        description=settings.DESCRIPTION,
        lifespan=lifespan
    )

    # app.include_router(public_api)

    return app