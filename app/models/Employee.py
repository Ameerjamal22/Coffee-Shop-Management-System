from peewee import *
from app.models.Base import BasePeeweeModel
import datetime


class Employee(BasePeeweeModel):
    """
    Database model for employees.
    """
    employee_id = BigAutoField(primary_key=True)
    first_name = CharField(max_length=50, null=False)
    last_name = CharField(max_length=50, null=False)
    email = CharField(unique=True, max_length=100, null=False)
    phone = CharField(max_length=20, null=True, unique=True, validators=[lambda phone: Employee.validate_phone(phone)])
    position = CharField(max_length=50, null=False)
    hire_date = DateField(default=datetime.date.today)
    creation_date = DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def validate_phone(phone: str):
        """
        Checks if the phone number contains digits only.
        """
        if not phone.isdigit():
            raise ValueError("Phone number must contain digits only.")
        return True
