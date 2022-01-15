# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.mockdata.salary_mockdata import all_seniority

router: APIRouter = APIRouter()


@router.get(
    path="/api/seniority",
    status_code=status.HTTP_200_OK,
    summary="Get levels availables.",
    tags=["Salaries"],
    response_model=List,
)
def titles():
    """
    # Seniority
    Get levels availables.

    # Parameters
    - None

    # Return
        List of all available levels.
    """
    return all_seniority()
