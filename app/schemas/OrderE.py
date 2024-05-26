from pydantic import BaseModel, Field, condecimal
from datetime import datetime
from app.schemas.CustomerE import CustomerOut
from app.schemas.EmployeeE import EmployeeOut


class OrderBase(BaseModel):
    """
    View base model for the order.
    """
    customer: CustomerOut = Field(..., description="the customer who placed the order", examples=[1])
    employee: EmployeeOut = Field(..., description="ID of the employee who took the order", examples=[1])
    total_price: condecimal(max_digits=10, decimal_places=2) = Field(..., ge=0, description="Total price of the order",
                                                                     examples=[19.99])
    status: str = Field(..., max_length=50, description="Status of the order", examples=["Pending"])

    class Config:
        orm_mode = True


class OrderOut(OrderBase):
    """
    View returned Order model.
    """
    order_id: int
    order_date: datetime = Field(default_factory=datetime.now, description="Date of the order",
                                 examples=[datetime.now()])


class OrderIn(OrderBase):
    """
    View input Order model.
    """
    pass
