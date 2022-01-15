# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.mockdata.salary_mockdata import all_technologies
from config import settings
from config.db import SessionLocal
from app.salaries.controllers import TechnologyController


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
    if not settings.MOCK_DATA:
        with SessionLocal() as db:
            controller = TechnologyController(db)
            technologies_db = controller.filter()
            return [technology.name for technology in technologies_db]
    return all_technologies()
