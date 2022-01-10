# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.mockdata.salary_mockdata import all_technologies


router: APIRouter = APIRouter()


@router.get(
    path="/api/technologies",
    status_code=status.HTTP_200_OK,
    summary="Get technologies availables.",
    tags=["Salaries"],
    response_model=List,
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
