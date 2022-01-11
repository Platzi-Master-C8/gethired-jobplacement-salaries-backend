
# FastAPI
from fastapi import APIRouter, Body
from fastapi import status

# Project
from sqlalchemy.orm import Query

from app.salaries.models.salaries import Salary, SalaryOut
from app.salaries.middlewares.data_validation import salary_by_knowledge
from app.salaries.schemas import Salary as SalaryModel
from app.utils.db import SessionLocal


router: APIRouter = APIRouter()


@router.post(
    path="/api/salaries",
    status_code=status.HTTP_200_OK,
    summary="Get salaries information.",
    response_model=SalaryOut,
    tags=["Salaries"]
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
    data = salary_by_knowledge(dict(salary_data))
    with SessionLocal() as db:
        salaries_db = db.query(SalaryModel).all()
    print(salaries_db)
    return SalaryOut(average=data["average"], top=data["top"], bottom=data["bottom"])
