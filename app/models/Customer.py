from app.models.Base import BasePeeweeModel
from peewee import *
import datetime


class Customer(BasePeeweeModel):
    """
    Customer database model stands for the end customer of the coffee shop  .
    """
    customer_id = AutoField(primary_key=True)
    first_name = CharField(max_length=50, null=False, blank=False)
    last_name = CharField(max_length=50, null=False, blank=False)
    email = CharField(unique=True, max_length=100, null=False, blank=False)
    phone = CharField(max_length=20, null=True)
    creation_date = DateTimeField(default=datetime.datetime.now)
