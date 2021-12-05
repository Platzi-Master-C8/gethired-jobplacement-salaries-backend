
# FastAPI
from fastapi import APIRouter, Body

# Project


router: APIRouter = APIRouter()


@router.get(
    "/api/technologies",
    summary="Get technologies availables.",
    response_model=Technology,
)
def salaries():
    """
    Salaries
    This is the main endpoint of the project.

    :argument salary_data: Salary
    :return: SalaryOut
    """
    return SalaryOut(average=4000, top=3000, bottom=5000)
