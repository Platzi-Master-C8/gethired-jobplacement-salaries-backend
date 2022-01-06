
# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.middlewares.data_validation import all_titles

router: APIRouter = APIRouter()


@router.get(
    path="/api/titles",
    status_code=status.HTTP_200_OK,
    summary="Get titles availables.",
    tags=["Salaries"],
)
def titles():
    """
    # Titles
    Get titles availables.

    # Parameters
    - None

    # Return
        List of all available titles.
    """
    return all_titles()
