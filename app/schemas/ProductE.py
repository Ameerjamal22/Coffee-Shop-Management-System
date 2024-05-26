from pydantic import BaseModel, Field, condecimal
from typing import Optional
from datetime import datetime
from app.schemas.CategoryE import CategoryOut


class ProductBase(BaseModel):
    """
    View base model for the product.
    """
    name: str = Field(..., min_length=1, max_length=80, description="Name of the product", examples=["Latte"])
    description: Optional[str] = Field(None, description="Description of the product",
                                       examples=["A rich and creamy coffee drink"])
    price: condecimal(max_digits=10, decimal_places=2) = Field(..., gt=0, description="Price of the product",
                                                               examples=[2.99])
    category: CategoryOut = Field(..., description="Category of the product")


class ProductOut(ProductBase):
    """
    View returned Product model.
    """
    product_id: int
    creation_date: datetime = Field(default_factory=datetime.now, description="Creation date of the product",
                                    examples=[datetime.now()])


class ProductIn(ProductBase):
    """
    View input Product model.
    """
    pass
