
# Python
from typing import List

# Pydantic
from pydantic import BaseModel, Field


class Salary(BaseModel):

    """
    Salary
    """

    english_level: str = Field(..., example="B2")
    seniority: str = Field(..., example="Mid")
    is_remote: bool = Field(..., example=True)
    location: str = Field(..., example="mx")
    title_id: str = Field(..., example="Fullstack")
    technologies: List = Field(..., example=["Python", "C"])


class SalaryOut(BaseModel):

    """
    Salary Out
    """

    average: int = Field(..., example="3000")
    top: int = Field(..., example="4000")
    bottom: int = Field(..., example="2000")


class SeniorityTextOut(BaseModel):
    level: str = Field(..., example="Junior")
    description: str = Field(..., example="0-3 years of...")


class SeniorityOut(BaseModel):
    """
    Seniority Out
    """
    title: str = Field(..., example="Seniority")
    texts: List[SeniorityTextOut] = Field(...)
    infoLink: str = Field(..., example="URL")


class EnglishTextOut(BaseModel):
    level: str = Field(..., example="A1")
    description: str = Field(..., example="Can understand and...")


class EnglishOut(BaseModel):
    """
    Seniority Out
    """
    title: str = Field(..., example="English Levels")
    texts: List[SeniorityTextOut] = Field(...)
    infoLink: str = Field(..., example="URL")
