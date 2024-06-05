from fastapi import APIRouter, Query, Path, Body
from app.helpers.CategoryHelper import *
from typing import Annotated

category_router: APIRouter = APIRouter()


@category_router.post("/categories/", tags=["categories", "-AdminUser"],
                      status_code=status.HTTP_201_CREATED,
                      response_model=CategoryGet)
async def create_category(category: CategoryPost) -> CategoryGet:
    """
    creates category and insert it into the database.
    ARGS:
        category (CategoryPost) : input category info as a model .
    """
    new_category: CategoryGet = create_category_helper(category)
    return new_category


@category_router.get("/categories/",
                     tags=["categories", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                     status_code=status.HTTP_200_OK,
                     response_model=list[CategoryGet])
async def get_categories(offset: Annotated[int, Query(..., ge=0, description="number of categories to skip")] = 0,
                         limit: Annotated[int, Query(..., ge=0, description='number of categories')] = 0
                         ) -> list[CategoryGet]:
    """
    get categories in the system .
    Args:
        offset(int): the index of the category to start from .
        limit(int): number of categories to be returned in the list .
    Returns:
        (list[CategoryGet]):list of category info in as category models .
    """
    categories: list[CategoryGet] = get_categories_helper(offset, limit)
    return categories


@category_router.get("/categories/{category_id}/",
                     tags=["categories", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                     status_code=status.HTTP_200_OK,
                     response_model=CategoryGet)
async def get_category(category_id: Annotated[int, Path(..., ge=0, description="id of the category to be returned")]
                       ) -> CategoryGet:
    """
    get the category that have the passed id from database .
    Args:
        category_id(int): the category id for the category that will be returned (if the id exist) .
    Returns:
        (CategoryGet): returns category as a pydantic model (CategoryGet) .
    """
    category: CategoryGet = get_category_helper(category_id)
    return category


@category_router.put("/categories/{category_id}",
                     tags=["categories", "-AdminUser"],
                     status_code=status.HTTP_200_OK,
                     response_model=CategoryGet)
async def update_category(
        category_id: Annotated[int, Path(..., ge=0, description="the id of the category to be updated")],
        category: Annotated[CategoryPost, Body(..., description="the new information of the category")]
) -> CategoryGet:
    """
    update the category with the passed id using the information passed as a pydantic model (CategoryPast) .
    Args:
        category_id(int): the id of the category to be updated .
        category(CategoryPost): the new info of the updated category .
    Returns:
        (CategoryGet): returns the new updated info of the category as a pydantic model (CategoryGet)
    """
    updated_category = update_category_helper(category_id, category)
    return updated_category


@category_router.delete("/categories/{category_id}",
                        tags=["categories", "-AdminUser"],
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: Annotated[int, Path(..., ge=0, description="the id of the category to delete")]):
    """
    deletes the category with the passed id .
    Args:
        category_id(int): the id of the category to be deleted .
    Returns:
        (CategoryGet): returns the new updated info of the category as a pydantic model (CategoryGet)
    """
    delete_category_helper(category_id)
