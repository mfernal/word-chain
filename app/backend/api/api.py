from fastapi import APIRouter
from app.backend.api.endpoints import users, games
from app.backend.core.settings import API


api_router = APIRouter()
api_router.include_router(
    users.router,
    prefix=API.USERS,
    tags=["users"]
)

api_router.include_router(
    games.router,
    prefix=API.GAMES,
    tags=["games"]
)
