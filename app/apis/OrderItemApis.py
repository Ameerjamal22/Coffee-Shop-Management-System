from fastapi import FastAPI, status

app: FastAPI = FastAPI() # used for testing .


@app.post("/orders/{order_id}/items/", tags=["orders", "AdminUser", "EmployeeUser"],
          status_code=status.HTTP_201_CREATED)
async def update_order_item():
    """
    not implemented yet
    """
    pass


@app.put("/orders/{order_id}/items/", tags=["orders", "AdminUser", "EmployeeUser"],
         status_code=status.HTTP_204_NO_CONTENT)
async def update_order_item():
    """
    not implemented yet
    """
    pass


@app.delete("/orders/{order_id}/items/", tags=["orders", "AdminUser", "EmployeeUser"],
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_item():
    """
    not implemented yet
    """
    pass
