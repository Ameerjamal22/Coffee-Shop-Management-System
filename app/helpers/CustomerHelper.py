from app.schemas.CustomerSchemas import CustomerPost, CustomerGet
from app.config.dbConfig import db
from app.models.Customer import Customer
from fastapi import HTTPException, status


@db.atomic()
def customer_email_exist(customer: CustomerPost) -> bool:
    """
    Checks if the customer email already exists in the database.
    Args:
        customer (CustomerPost): Customer input whose email will be checked.
    Returns (bool): True if the email already exists, false otherwise.
    """
    email_exists: bool = Customer.select().where(Customer.email == customer.email).exists()
    return email_exists


@db.atomic()
def create_customer_helper(customer: CustomerPost) -> CustomerGet:
    """
    Creates a customer and inserts it into the database.
    Args:
        customer (CustomerPost): Input customer data (Pydantic model object).
    Returns:
        CustomerGet: The created customer as a Pydantic model.
    """
    email_exists: bool = customer_email_exist(customer)

    if email_exists:
        raise HTTPException(detail="Customer email already exists, failed to create customer object",
                            status_code=status.HTTP_409_CONFLICT)

    customer_data: dict = customer.model_dump()
    new_customer: Customer = Customer(**customer_data)
    new_customer.save()

    return CustomerGet.from_orm(new_customer)


@db.atomic()
def get_customers_helper(offset: int, limit: int) -> list[CustomerGet]:
    """
    Gets customers from the database.
    Args:
        offset (int): Number of customers to skip.
        limit (int): Number of customers to return.
    Returns:
        list[CustomerGet]: List of customers returned as Pydantic models.
    """
    customers = list(Customer.select().limit(limit).offset(offset))
    customers = [CustomerGet.from_orm(customer) for customer in customers]
    return customers


@db.atomic()
def customer_id_exist(customer_id: int) -> bool:
    """
    Checks if the customer ID exists in the database.
    Args:
        customer_id (int): Customer ID to be checked.
    Returns:
        (bool): True if the customer ID exists, false otherwise.
    """
    exists: bool = Customer.select().where(Customer.customer_id == customer_id).exists()
    return exists


@db.atomic()
def get_customer_helper(customer_id: int) -> CustomerGet:
    """
    Gets a customer from the database using their ID.
    Args:
        customer_id (int): The ID of the customer to retrieve from the database.
    Returns:
        (CustomerGet): Customer data as a Pydantic model.
    """
    if not customer_id_exist(customer_id):
        raise HTTPException(detail="There is no customer with the passed ID, check the ID",
                            status_code=status.HTTP_404_NOT_FOUND)

    customer = CustomerGet.from_orm(Customer.select().where(Customer.customer_id == customer_id).get())
    return customer


@db.atomic()
def update_customer_helper(customer_id: int, customer: CustomerPost) -> CustomerGet:
    """
    Updates a customer in the database.
    Args:
        customer_id (int): The ID of the customer to update.
        customer (CustomerPost): The new data for the customer (Pydantic model object).
    Returns:
        CustomerGet: Updated customer data as a Pydantic model.
    """
    if not customer_id_exist(customer_id):
        raise HTTPException(detail="There is no customer with the passed ID, check the ID",
                            status_code=status.HTTP_404_NOT_FOUND)

    customer_data: dict = customer.model_dump()
    query = Customer.update(customer_data).where(Customer.customer_id == customer_id)
    query.execute()

    updated_customer = CustomerGet.from_orm(Customer.select().where(Customer.customer_id == customer_id).get())
    return updated_customer


@db.atomic()
def delete_customer_helper(customer_id: int) -> None:
    """
    Deletes a customer from the database.
    Args:
        customer_id (int): The ID of the customer to delete.
    """
    if not customer_id_exist(customer_id):
        raise HTTPException(detail="There is no customer with the passed ID, check the ID",
                            status_code=status.HTTP_404_NOT_FOUND)

    query = Customer.delete().where(Customer.customer_id == customer_id)
    query.execute()
