from fastapi import APIRouter, status, Path, Query, Body
from app.schemas.CustomerSchemas import CustomerPost, CustomerGet
from app.helpers.CustomerHelper import *
from typing import Annotated

customer_router: APIRouter = APIRouter()


@customer_router.post("/customers/", tags=["customers", "-AdminUser", "-CustomerUser", "-EmployeeUser"],
                      status_code=status.HTTP_201_CREATED,
                      response_model=CustomerGet)
async def create_category(customer: CustomerPost) -> CustomerGet:
    """
    creates customer and insert it into the database.
    ARGS:
        customer (CustomerPost) : input customer info as a model .
    """
    new_customer: CustomerPost = create_customer_helper(customer)
    return new_customer


@customer_router.get("/customers/{customer_id}/",
                     tags=["customers", "-AdminUser", "-CustomerUser"],
                     status_code=status.HTTP_200_OK,
                     response_model=CustomerGet
                     )
async def get_customer(customer_id: Annotated[int, Path(..., ge=0, description="the id of the customer to get")]):
    """
    get the customer with the passed customer id .
    Args:
        customer_id(int): the id of the customer to get .
    Returns:
        (CustomerGet): returns the customer info as a pydantic model (CustomerGet)
    """
    customer = get_customer_helper(customer_id)
    return customer


@customer_router.get("/customers/",
                     tags=["customers", "-AdminUser"],
                     status_code=status.HTTP_200_OK,
                     response_model=list[CustomerGet])
async def get_customers(offset: Annotated[int, Query(..., ge=0, description="the number of customers to skip")],
                        limit: Annotated[int, Query(..., ge=0, description="the number of customers to get")]):
    """
    get categories in the system .
    Args:
        offset(int): the index of the customer to start from .
        limit(int): number of customers to be returned in the list .
    Returns:
        (list[CustomerGet]):list of Customers info in as Customer models .
    """
    customers = get_customers_helper(offset, limit)
    return customers


@customer_router.put("/customers/{customer_id}/",
                     tags=["customers", "-AdminUser", "-CustomerUser"],
                     status_code=status.HTTP_202_ACCEPTED,
                     response_model=CustomerGet)
async def update_customer(
        customer_id: Annotated[int, Path(..., ge=0, description="the id of the customer to be updated")],
        customer: Annotated[CustomerPost, Body(..., description="the new information of the customer")]):
    """
    update the customer with the passed id using the information passed as a pydantic model (CustomerPast) .
    Args:
        customer_id(int): the id of the customer to be updated .
        customer(CustomerPost): the new info of the updated customer .
    Returns:
        (CustomerGet): returns the new updated info of the customer as a pydantic model (CustomerGet)
    """
    updated_customer = update_customer_helper(customer_id, customer)
    return updated_customer


@customer_router.delete("/customers/{customer_id}/",
                        tags=["customers", "-AdminUser", "-CustomerUser"],
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(
        customer_id: Annotated[int, Path(..., ge=0, description="the id of the customer to be deleted")]):
    """
    deletes the customer with the passed id .
    Args:
        customer_id(int): the id of the customer to be deleted .
    """
    delete_customer_helper(customer_id)

