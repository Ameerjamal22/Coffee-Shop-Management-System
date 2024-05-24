from peewee import *
from app.models.Base import BasePeeweeModel


class Category(BasePeeweeModel):
    """
    Database model to represent product categories .
    """
    category_id = BigAutoField(primary_key=True)
    name = CharField(max_length=50, null=False, blank=False, unique=True)
    description = CharField(max_length=100, null=True)
