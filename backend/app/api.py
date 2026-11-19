from fastapi import APIRouter

from app.movies.api.router import router as movies_router
from app.users.api.router import router as users_router
from app.auth.api.router import router as auth_router
from app.lists.api.router import router as lists_router
from app.ratings.api.router import router as ratings_router
from app.recommendations.api.router import router as recommendations_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(movies_router)
api_router.include_router(users_router)
api_router.include_router(auth_router)
api_router.include_router(lists_router)
api_router.include_router(ratings_router)
api_router.include_router(recommendations_router)