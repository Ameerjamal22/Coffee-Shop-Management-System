from fastapi import FastAPI, status

app: FastAPI = FastAPI()


@app.get("/employees/{employee_id}/", tags=["employees", "AdminUser", "EmployeeUser"],
         status_code=status.HTTP_200_OK)
async def get_employee():
    """
    not implemented yet .
    """
    pass


@app.get("/employees/", tags=["employees", "AdminUser"],
         status_code=status.HTTP_200_OK)
async def get_employee():
    """
    not implemented yet .
    """
    pass


@app.put("/employees/{employee_id}/", tags=["employees", "AdminUser"],
         status_code=status.HTTP_204_NO_CONTENT)
async def update_employee():
    """
    not implemented yet .
    """
    pass


@app.delete("/employees/{employee_id}/", tags=["employees", "AdminUser"],
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee():
    """
    not implemented yet .
    """
    pass
