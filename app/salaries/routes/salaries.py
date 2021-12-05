
# FastAPI
from fastapi import APIRouter, Body

# Project
from app.salaries.schemas import Salary, SalaryOut


router: APIRouter = APIRouter()


@router.get(
    "/api/salaries",
    summary="Get salaries information.",
    response_model=SalaryOut,
)
def salaries(salary_data: Salary = Body(...)):
    """
    Salaries
    This is the main endpoint of the project.

    :argument salary_data: Salary
    :return: SalaryOut
    """
    return SalaryOut(average=4000, top=3000, bottom=5000)
