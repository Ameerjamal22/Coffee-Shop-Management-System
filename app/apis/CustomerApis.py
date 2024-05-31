from fastapi import FastAPI, status

app: FastAPI = FastAPI()


@app.get("/customers/{customer_id}", tags=["customers", "AdminUser", "CustomerUser"],
         status_code=status.HTTP_200_OK)
async def get_customer():
    """
    not implemented yet .
    """
    pass


@app.put("/customers/{customer_id}", tags=["customers", "AdminUser", "CustomerUser"],
         status_code=status.HTTP_204_NO_CONTENT)
async def update_customer():
    """
    not implemented yet .
    """
    pass


@app.delete("/customers/{customer_id}", tags=["customers", "AdminUser", "CustomerUser"],
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer():
    """
    not implemented yet .
    """
    pass
