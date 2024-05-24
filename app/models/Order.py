from peewee import *
from app.models.Customer import Customer
from app.models.Employee import Employee
from app.models.Base import BasePeeweeModel
import datetime


class Order(BasePeeweeModel):
    """
    Database model that represents the customer order .
    """
    order_id = BigAutoField(primary_key=True)
    customer = ForeignKeyField(Customer, backref="orders", on_delete="CASCADE", null=False, on_update='CASCADE')
    employee = ForeignKeyField(Employee, backref="takes", on_delete="CASCADE", null=False, on_update="CASCADE")
    order_date = DateTimeField(default=datetime.datetime.now())
    total_price = DecimalField(max_digits=10, decimal_places=2, null=False)
    status = CharField(max_length=50, choices=["Pending", "Completed", "UnAvailable"], null=False)
