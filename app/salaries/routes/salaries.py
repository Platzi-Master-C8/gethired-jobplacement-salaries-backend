
# FastAPI
from fastapi import APIRouter, Body, HTTPException
from fastapi import status

# Project
from app.salaries.models.salaries import Salary, SalaryOut
from app.salaries.mockdata.salary_mockdata import salary_mokedata, all_seniority, all_titles, all_english_levels, all_technologies


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

    if not salary_data.seniority in all_seniority():
        raise HTTPException(
            status_code=404, detail=f"Seniority {salary_data.seniority} not found")

    if not salary_data.title_id in all_titles():
        raise HTTPException(
            status_code=404, detail=f"Title {salary_data.title_id} not found")

    if not salary_data.english_level in all_english_levels():
        raise HTTPException(
            status_code=404, detail=f"English Level {salary_data.english_level} not found")

    for technlogy in salary_data.technologies:
        individual_tech = dict(technlogy)
        individual_tech = individual_tech["name"]
        if not individual_tech in all_technologies():
            raise HTTPException(
                status_code=404, detail=f"Technology {individual_tech} not found")

    data = salary_mokedata()

    return SalaryOut(average=data["average"], top=data["top"], bottom=data["bottom"])
