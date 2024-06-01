from fastapi import APIRouter, Depends
from app.helpers.CategoryHelper import *

category_router: APIRouter = APIRouter()


@category_router.post("/categories/", tags=["categories", "-AdminUser"], status_code=status.HTTP_201_CREATED)
async def create_category(_: None = Depends(create_category_dependency)):
    """
    creates category and insert it into the database.
    """


@category_router.get("/categories/", tags=["categories", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                     status_code=status.HTTP_200_OK)
async def get_categories():
    """
    not implemented yet
    """
    pass


@category_router.get("/categories/{category_id}/", tags=["categories", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                     status_code=status.HTTP_200_OK)
async def get_category():
    """
    not implemented yet
    """
    pass


@category_router.put("/categories/{category_id}", tags=["categories", "-AdminUser"],
                     status_code=status.HTTP_204_NO_CONTENT)
async def update_category():
    """
    not implemented yet
    """
    pass


@category_router.delete("/categories/{category_id}", tags=["categories", "-AdminUser"],
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_category():
    """
    not implemented yet
    """
    pass
