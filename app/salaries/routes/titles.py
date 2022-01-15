# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from app.salaries.mockdata.salary_mockdata import all_titles
from app.salaries.controllers import TitleController
from config import settings
from config.db import SessionLocal

router: APIRouter = APIRouter()


@router.get(
    path="/api/titles",
    status_code=status.HTTP_200_OK,
    summary="Get titles availables.",
    tags=["Salaries"],
    response_model=List,
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
    if not settings.MOCK_DATA:
        with SessionLocal() as db:
            return [title.name for title in TitleController(db).filter()]
    return all_titles()
