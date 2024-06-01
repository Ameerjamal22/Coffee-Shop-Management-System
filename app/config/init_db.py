from app.config.dbConfig import db
from app.models.Category import Category
from app.models.Order import Order
from app.models.Employee import Employee
from app.models.Customer import Customer
from app.models.OrderItem import OrderItem
from app.models.Product import Product
from app.models.Inventory import Inventory

db.connect()
db.create_tables([Category, Order, Employee, Customer, OrderItem, Product, Inventory])
db.close()
