from fastapi import FastAPI, status

app: FastAPI = FastAPI()


@app.post("/categories/", tags=["categories", "AdminUser"], status_code=status.HTTP_201_CREATED)
async def create_category():
    """
    not implemented yet .
    """
    pass


@app.get("/categories/", tags=["categories", "AdminUser", "CustomerUser", "EmployeeUser"],
         status_code=status.HTTP_200_OK)
async def get_categories():
    """
    not implemented yet
    """
    pass


@app.get("/categories/{category_id}/", tags=["categories", "AdminUser", "CustomerUser", "EmployeeUser"],
         status_code=status.HTTP_200_OK)
async def get_category():
    """
    not implemented yet
    """
    pass


@app.put("categories/{category_id}", tags=["categories", "AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def update_category():
    """
    not implemented yet
    """
    pass


@app.delete("categories/{category_id}", tags=["categories", "AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_category():
    """
    not implemented yet
    """
    pass
