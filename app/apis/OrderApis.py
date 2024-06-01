from fastapi import APIRouter, status

order_router: APIRouter = APIRouter()


@order_router.post("/orders/", tags=["orders", "-AdminUser", "-EmployeeUser"],
                   status_code=status.HTTP_201_CREATED)
async def create_order():
    """
    not yet implemented
    """
    pass


@order_router.get("/orders/", tags=["orders", "-AdminUser", "-EmployeeUser"], status_code=status.HTTP_200_OK)
async def get_orders():
    """
    not yet implemented
    """
    pass


@order_router.get("/orders/{order_id}/", tags=["orders", "-AdminUser", "-EmployeeUser"],
                  status_code=status.HTTP_200_OK)
async def get_order():
    """
    not implemented yet
    """
    pass


@order_router.put("/orders/{order_id}/", tags=["orders", "-AdminUser", "-EmployeeUser"],
                  status_code=status.HTTP_204_NO_CONTENT)
async def update_order():
    """
    not yet implemented
    """
    pass


@order_router.delete("/orders/{order_id}/", tags=["orders", "-AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_order():
    """
    not yet implemented
    """
    pass
