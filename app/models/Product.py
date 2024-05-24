from app.models.Base import BasePeeweeModel
from peewee import *
from app.models.Category import Category
import datetime


class Product(BasePeeweeModel):
    """
    Database model for product contains related details about the product .
    """
    product_id = BigAutoField(primary_key=True)
    name = CharField(unique=True, null=False, blank=False, max_length=80)
    description = TextField(null=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKeyField(Category, backref="products", on_delete="CASCADE", null=False)
    creation_date = DateTimeField(default=datetime.datetime.now())
