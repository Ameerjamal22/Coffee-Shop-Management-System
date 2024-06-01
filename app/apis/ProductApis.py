from fastapi import APIRouter, status

product_router: APIRouter = APIRouter()  # used for testing .


@product_router.post("/products/", tags=["products", "-AdminUser"], status_code=status.HTTP_201_CREATED)
async def create_product():
    """
    not yet implemented
    """
    pass


@product_router.get("/products/", tags=["products", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                    status_code=status.HTTP_200_OK)
async def get_all_products():
    """
    not implemented yet
    """
    pass


@product_router.get("/products/{product_id}/", tags=["products", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                    status_code=status.HTTP_200_OK)
async def get_product():
    """
    not yet implemented
    """
    pass


@product_router.put("/products/{product_id}/", tags=["products", "-AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def update_product():
    """
    not yet implemented
    """
    pass


@product_router.delete("/products/{product_id}/", tags=["products", "-AdminUser"],
                       status_code=status.HTTP_204_NO_CONTENT)
async def delete_product():
    """
    not yet implemented
    """
    pass


@product_router.get("/products/search/", tags=["products", "-AdminUser", "-EmployeeUser", "-CustomerUser"],
                    status_code=status.HTTP_200_OK)
async def search_products():
    """
    not yet implemented ( search with filters ) .
    """
    pass
