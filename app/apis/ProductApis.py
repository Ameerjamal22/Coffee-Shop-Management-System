from fastapi import FastAPI, status

app: FastAPI = FastAPI()  # used for testing .


@app.post("/products/", tags=["products", "AdminUser"], status_code=status.HTTP_201_CREATED)
async def create_product():
    """
    not yet implemented
    """
    pass


@app.get("/products/", tags=["products", "AdminUser", "CustomerUSer", "EmployeeUser"],
         status_code=status.HTTP_200_OK)
async def get_all_products():
    """
    not implemented yet
    """
    pass


@app.get("/products/{product_id}/", tags=["products", "AdminUser", "CustomerUSer", "EmployeeUser"],
         status_code=status.HTTP_200_OK)
async def get_product():
    """
    not yet implemented
    """
    pass


@app.put("/products/{product_id}/", tags=["products", "AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def update_product():
    """
    not yet implemented
    """
    pass


@app.delete("/products/{product_id}/", tags=["products", "AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_product():
    """
    not yet implemented
    """
    pass


@app.get("/products/search", tags=["products", "AdminUser", "EmployeeUser", "CustomerUser"],
         status_code=status.HTTP_200_OK)
async def search_products():
    """
    not yet implemented ( search with filters ) .
    """
    pass
