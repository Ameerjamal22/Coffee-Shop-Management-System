from fastapi import APIRouter, status

order_item_router: APIRouter = APIRouter()


@order_item_router.post("/orders/{order_id}/items/", tags=["orders", "-AdminUser", "-EmployeeUser"],
                        status_code=status.HTTP_201_CREATED)
async def create_order_item():
    """
    not implemented yet
    """
    pass


@order_item_router.put("/orders/{order_id}/items/", tags=["orders", "-AdminUser", "-EmployeeUser"],
                       status_code=status.HTTP_204_NO_CONTENT)
async def update_order_item():
    """
    not implemented yet
    """
    pass


@order_item_router.delete("/orders/{order_id}/items/", tags=["orders", "-AdminUser", "-EmployeeUser"],
                          status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_item():
    """
    not implemented yet
    """
    pass
