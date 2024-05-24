from peewee import *
from app.models.Base import BasePeeweeModel
from app.models.Product import Product
import datetime


class Inventory(BasePeeweeModel):
    """
    Database model that stands for inventory and its contents .
    """
    inventory_id = BigAutoField(primary_key=True)
    product = ForeignKeyField(Product, backref='inventory', null=False, unique=True)
    quantity_in_stock = IntegerField(null=False, default=0)
    last_updated = DateTimeField(default=datetime.datetime.now())
