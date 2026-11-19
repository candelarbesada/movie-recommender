from fastapi import APIRouter

router = APIRouter(prefix="/lists", tags=["Lists"])


@router.get("/")
def get_lists():
    return {"message": "Lists endpoint works"}