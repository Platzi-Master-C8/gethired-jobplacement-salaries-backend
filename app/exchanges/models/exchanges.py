# Python
from typing import List

# Pydantic
from pydantic import BaseModel, Field


class Currency(BaseModel):
    """
    Currency
    """
    currency: str = Field(..., example="COP")
    name: str = Field(..., example="Colombian Peso")
    country: str = Field(..., example="Colombia")


class Exchange(BaseModel):
    """
    Exchange Input
    """
    initial_value: int = Field(..., example="200")
    change_to: str = Field(..., example="COP")


class ExchangeOut(BaseModel):
    """
    Exchange Output
    """
    value: int = Field(..., example="200")
