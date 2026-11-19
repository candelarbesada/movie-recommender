from fastapi import APIRouter

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/")
def get_movies():
    return {"message": "Movies endpoint works"}