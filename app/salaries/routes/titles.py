
# FastAPI
from fastapi import APIRouter, Body

# Project


router: APIRouter = APIRouter()


@router.get(
    "/api/titles",
    summary="Get titles availables.",
    tags=["Salaries"]
)
def titles():
    """
    Titles
    Get titles availables.
    """
    return [dict(name="backend developer"), dict("frontend developer")]
