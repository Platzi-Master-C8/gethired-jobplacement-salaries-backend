
# FastAPI
from fastapi import APIRouter, Body

# Project


router: APIRouter = APIRouter()


@router.get(
    "/api/technologies",
    summary="Get technologies availables.",
)
def technologies():
    """
    Technologies
    Get technologies available in our data set.
    """
    return [dict(name="python"), dict("javascript")]
