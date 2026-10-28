from pydantic import BaseModel, Field
from typing import Optional


class IngredientCreate(BaseModel):
    name: str = Field(..., min_length=2)
    category: str
    unit: str
    description: Optional[str] = None


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    unit: Optional[str] = None
    description: Optional[str] = None