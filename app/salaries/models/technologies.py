
# Python
from typing import List

# Pydantic
from pydantic import BaseModel, Field


class Technology(BaseModel):
    name: str = Field(..., example="Python")
