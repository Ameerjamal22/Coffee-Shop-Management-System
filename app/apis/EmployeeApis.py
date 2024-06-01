from fastapi import APIRouter, status

employee_router: APIRouter = APIRouter()


@employee_router.get("/employees/{employee_id}/", tags=["employees", "-AdminUser", "-EmployeeUser"],
                     status_code=status.HTTP_200_OK)
async def get_employee():
    """
    not implemented yet .
    """
    pass


@employee_router.get("/employees/", tags=["employees", "-AdminUser"],
                     status_code=status.HTTP_200_OK)
async def get_employee():
    """
    not implemented yet .
    """
    pass


@employee_router.put("/employees/{employee_id}/", tags=["employees", "-AdminUser"],
                     status_code=status.HTTP_204_NO_CONTENT)
async def update_employee():
    """
    not implemented yet .
    """
    pass


@employee_router.delete("/employees/{employee_id}/", tags=["employees", "-AdminUser"],
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee():
    """
    not implemented yet .
    """
    pass
