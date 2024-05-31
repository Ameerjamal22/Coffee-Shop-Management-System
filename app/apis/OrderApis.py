from fastapi import FastAPI, status

app: FastAPI = FastAPI() # used for testing .


@app.post("/orders/", tags=["orders", "AdminUser", "EmployeeUser"],
          status_code=status.HTTP_201_CREATED)
async def create_order():
    """
    not yet implemented
    """
    pass


@app.get("/orders/", tags=["orders", "AdminUser", "EmployeeUser"], status_code=status.HTTP_200_OK)
async def get_orders():
    """
    not yet implemented
    """
    pass


@app.get("/orders/{order_id}/", tags=["orders", "AdminUser", "EmployeeUser"],
         status_code=status.HTTP_200_OK)
async def get_order():
    """
    not implemented yet
    """
    pass


@app.put("/orders/{order_id}/", tags=["orders", "AdminUser", "EmployeeUser"],
         status_code=status.HTTP_204_NO_CONTENT)
async def update_order():
    """
    not yet implemented
    """
    pass


@app.delete("/orders/{order_id}/", tags=["orders", "AdminUser"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_order():
    """
    not yet implemented
    """
    pass
