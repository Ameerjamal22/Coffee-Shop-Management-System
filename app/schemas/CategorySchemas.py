from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    """
    View base model for the category .
    """
    name: str = Field(..., min_length=2, max_length=50, description="Name of the category", examples=["refreshers"])
    description: Optional[str] = Field(None, max_length=100, description="Description of the category",
                                       examples=["juice to refresh yourself"])

    class Config:
        from_attributes = True


class CategoryGet(CategoryBase):
    """
    View returned Category model (returned to the user) .
    """
    category_id: int


class CategoryPost(CategoryBase):
    """
    View input Category model (used for creation) .
    """
    pass
