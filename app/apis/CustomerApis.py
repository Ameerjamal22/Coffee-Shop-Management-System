from fastapi import APIRouter, status

customer_router: APIRouter = APIRouter()


@customer_router.get("/customers/{customer_id}/", tags=["customers", "-AdminUser", "-CustomerUser"],
                     status_code=status.HTTP_200_OK)
async def get_customer():
    """
    not implemented yet .
    """
    pass


@customer_router.get("/customers/", tags=["customers", "-AdminUser"],
                     status_code=status.HTTP_200_OK)
async def get_customer():
    """
    not implemented yet .
    """
    pass


@customer_router.put("/customers/{customer_id}/", tags=["customers", "-AdminUser", "-CustomerUser"],
                     status_code=status.HTTP_204_NO_CONTENT)
async def update_customer():
    """
    not implemented yet .
    """
    pass


@customer_router.delete("/customers/{customer_id}/", tags=["customers", "-AdminUser", "-CustomerUser"],
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer():
    """
    not implemented yet .
    """
    pass
