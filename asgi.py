import uvicorn

from src.app import create_app
from src.config import settings 

api = create_app(settings=settings)

if __name__ == "__main__":
    uvicorn.run(
        "asgi:api",
        host="0.0.0.0",
        port=8000,
        reload=True
    )