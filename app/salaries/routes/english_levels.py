# Python
from typing import List
# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.models.salaries import EnglishOut
from app.salaries.mockdata.salary_mockdata import all_english_levels

router: APIRouter = APIRouter()


@router.get(
    path="/api/english",
    status_code=status.HTTP_200_OK,
    summary="Get english levels.",
    tags=["Salaries"],
    response_model=EnglishOut,
)
def titles():
    """
    # English levels
    Get levels availables.

    # Parameters
    - None

    # Return
        List of all available english levels with description.
    """
    return all_english_levels()
