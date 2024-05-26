from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
import re
from datetime import datetime


class CustomerBase(BaseModel):
    """
    The customer Base view model .
    """
    first_name: str = Field(..., min_length=1, max_length=50, description="First name of the customer",
                            examples=["ameer"])
    last_name: str = Field(..., min_length=2, max_length=50, description="Last name of the customer",
                           examples=["ameer"])
    email: EmailStr = Field(..., description="Email address of the customer", examples=["user@example.com"])
    phone: Optional[str] = Field(None, max_length=20, description="Phone number of the customer",
                                 examples=["+970594123451"])

    @staticmethod
    @field_validator('phone')
    def validate_phone(value: str):
        if value and not re.match(r'^\+?[0-9\s\-]+$', value):
            raise ValueError("Phone number must be a valid phone number")
        return value


class CustomerOut(CustomerBase):
    """
    View Customer to be returned .
    """
    customer_id: int
    creation_date: datetime = Field(default_factory=datetime.now, description="Creation date of the customer record",
                                    examples=[datetime.now()])


class CustomerIn(CustomerBase):
    """
    View customer model that will be passed as an input .
    """
    pass
