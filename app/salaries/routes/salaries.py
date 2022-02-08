# FastAPI
from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from starlette import status

# Project
from sqlalchemy.orm import Query
from config import settings
from config.db import SessionLocal
from app.salaries.controllers import SalaryController, TitleController
from app.salaries.models.salaries import Salary, SalaryOut
from app.salaries.mockdata.salary_mockdata import (
    salary_mokedata,
    all_seniority,
    all_titles,
    all_english_levels,
    all_technologies,
)


router: APIRouter = APIRouter()


@router.post(
    path="/api/salaries",
    status_code=status.HTTP_200_OK,
    summary="Get salaries information.",
    response_model=SalaryOut,
    tags=["Salaries"],
)
def salaries(salary_data: Salary = Body(...)):
    """
    # Salaries
    This is the main endpoint of the project.

    # Parameters
    - salary_data: Salary -> Salary Model.

    # Return
        SalaryOut Model -> Values of average, top and bottom.
    """

    if not settings.MOCK_DATA:
        with SessionLocal() as db:
            if not TitleController(db).filter(name=salary_data.title_name).first():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Title {salary_data.title_name} not found"
                )
            return SalaryController(db).calculate_salary(salary_data)

    if salary_data.seniority not in all_seniority():
        raise HTTPException(
            status_code=404, detail=f"Seniority {salary_data.seniority} not found"
        )

    if salary_data.title_name not in all_titles():
        raise HTTPException(
            status_code=404, detail=f"Title {salary_data.title_name} not found"
        )

    if salary_data.english_level not in all_english_levels():
        raise HTTPException(
            status_code=404,
            detail=f"English Level {salary_data.english_level} not found",
        )

    for tech in salary_data.technologies:
        if tech not in all_technologies():
            raise HTTPException(status_code=404, detail=f"Technology {tech} not found")

    data = salary_mokedata()
    return SalaryOut(average=data["average"], top=data["top"], bottom=data["bottom"])
