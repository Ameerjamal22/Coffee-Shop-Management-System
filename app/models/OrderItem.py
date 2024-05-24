from peewee import *
from app.models.Base import BasePeeweeModel
from app.models.Order import Order
from app.models.Product import Product


class OrderItem(BasePeeweeModel):
    """
    Database model that represent a part of an order that (one item and its quantity) .
    """
    order_item_id = BigAutoField(PrimaryKeyField=True)
    order = ForeignKeyField(Order, backref='in', on_delete="Cascade", on_update="CASCADE", null=False)
    product = ForeignKeyField(Product, backref='of type', on_delete="Cascade", on_update="CASCADE", null=False)
    quantity = IntegerField(default=1)
    unit_price = DecimalField(max_digits=10, decimal_places=2, null=False)
    total_price = DecimalField(max_digits=10, decimal_places=2, null=False)
