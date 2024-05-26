from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    """
    View base model for the category .
    """
    name: str = Field(..., min_length=2, max_length=50, description="Name of the category", examples=["refreshers"])
    description: Optional[str] = Field(None, max_length=100, description="Description of the category",
                                       examples=["juice to refresh yourself"])


class CategoryOut(CategoryBase):
    """
    View returned Category model .
    """
    category_id: int


class CategoryIn(CategoryBase):
    """
    View input Category model .
    """
    pass
