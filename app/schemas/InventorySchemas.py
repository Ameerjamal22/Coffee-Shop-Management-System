from pydantic import BaseModel, Field
from datetime import datetime
from app.schemas.ProductSchemas import ProductOut


class InventoryBase(BaseModel):
    """
    View base model for the inventory.
    """
    product: ProductOut = Field(description="the product that the inventory record instance contains .")
    quantity_in_stock: int = Field(..., ge=0, description="Quantity of the product in stock", examples=[100])

    class Config:
        orm_mode = True


class InventoryOut(InventoryBase):
    """
    View returned Inventory model.
    """
    inventory_id: int
    last_updated: datetime = Field(default_factory=datetime.now, description="Last updated timestamp of the inventory",
                                   examples=[datetime.now()])


class InventoryIn(InventoryBase):
    """
    View input Inventory model.
    """
    pass
