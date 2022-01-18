from fastapi import APIRouter
from routes.endpoints import home
from routes.endpoints import item

api_router = APIRouter()
api_router.include_router(home.router)
api_router.include_router(item.router)
