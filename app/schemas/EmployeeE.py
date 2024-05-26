from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
import re
from datetime import datetime, date


class EmployeeBase(BaseModel):
    """
    View base model for the employee.
    """
    first_name: str = Field(..., min_length=1, max_length=50, description="First name of the employee",
                            examples=["ameer"])
    last_name: str = Field(..., min_length=1, max_length=50, description="Last name of the employee",
                           examples=["rabie"])
    email: EmailStr = Field(..., description="Email address of the employee", examples=["employee@example.com"])
    phone: Optional[str] = Field(None, max_length=20, description="Phone number of the employee",
                                 examples=["+970594123451"])
    position: str = Field(..., max_length=50, description="Position of the employee", examples=["Manager"])

    @staticmethod
    @field_validator('phone')
    def validate_phone(value: str):
        if value and not re.match(r'^\+?[0-9\s\-]+$', value):
            raise ValueError("Phone number must be a valid phone number")
        return value

    class Config:
        orm_mode = True


class EmployeeOut(EmployeeBase):
    """
    View returned Employee model.
    """
    employee_id: int
    hire_date: date = Field(default_factory=date.today, description="Hire date of the employee",
                            examples=[date.today()])
    creation_date: datetime = Field(default_factory=datetime.now, description="Creation date of the employee record",
                                    examples=[datetime.now()])


class EmployeeIn(EmployeeBase):
    """
    View input Employee model.
    """
    pass
