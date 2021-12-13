
# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.middlewares.data_validation import all_technologies


router: APIRouter = APIRouter()


@router.get(
    path="/api/technologies",
    status_code=status.HTTP_200_OK,
    summary="Get technologies availables.",
    tags=["Salaries"]
)
def technologies():
    """
    # Technologies
    Get technologies available in our data set.

    # Parameters
    - None

    # Return
        List of all available technologies.
    """
    return all_technologies()
