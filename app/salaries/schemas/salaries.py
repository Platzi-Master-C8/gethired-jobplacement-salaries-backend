
# Python
from typing import List

# Pydantic
from pydantic import BaseModel, Field, validator

# Project
from .technologies import Technology


A1 = "A1"
A2 = "A2"
B1 = "B1"
B2 = "B2"
C1 = "C1"
C2 = "C2"

ENGLISH_LEVEL = (
    (A1, "A1 Beginner"),
    (A2, "A2 Elementary"),
    (B1, "B1 Intermediate"),
    (B2, "B2 Upper Intermediate"),
    (C1, "C1 Advance"),
    (C2, "C2 Upper Advance"),
)


class Salary(BaseModel):

    """
    Salary
    """

    english_level: str = Field(..., example="B2")
    seniority: int = Field(..., example="1")
    is_remote: bool = Field(..., example=False)
    location: str = Field(..., example="mx")
    title_id: str = Field(..., example="24")
    technologies: List[str] = Field(...)


class SalaryOut(BaseModel):

    """
    Salary Out
    """

    average: int = Field(..., example="3000")
    top: int = Field(..., example="4000")
    bottom: int = Field(..., example="2000")
