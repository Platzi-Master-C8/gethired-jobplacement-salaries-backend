# Python
from typing import List

# Pydantic
from pydantic import BaseModel, Field


class Salary(BaseModel):

    """
    Salary
    """

    english_level: str = Field(..., example="B2")
    seniority: int = Field(..., example="1")
    is_remote: bool = Field(..., example=True)
    location: str = Field(..., example="mx")
    title_name: str = Field(..., example="Frontend Developer")
    technologies: List = Field(..., example=["Python", "JavaScript"])


class SalaryOut(BaseModel):

    """
    Salary Out
    """

    average: int = Field(..., example="3000")
    top: int = Field(..., example="4000")
    bottom: int = Field(..., example="2000")
