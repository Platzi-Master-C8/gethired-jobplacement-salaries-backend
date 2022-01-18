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


class ExchangeOut(BaseModel):
    """
    Exchange Output
    """
    converted_currency: List = Field(..., example=[2000, 100, 4000])
