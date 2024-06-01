from fastapi import status, APIRouter

report_router: APIRouter = APIRouter()


@report_router.get("/reports/sales/daily/", tags=["reports", "-AdminUser", "-EmployeeUser"],
                   status_code=status.HTTP_200_OK)
async def get_daily_sales():
    """
    not implemented yet .
    """
    pass


@report_router.get("/reports/sales/monthly/", tags=["reports", "-AdminUser", "-EmployeeUser"],
                   status_code=status.HTTP_200_OK)
async def get_monthly_sales():
    """
    not implemented yet
    """
    pass


@report_router.get("/reports/sales/annual/", tags=["reports", "-AdminUser", "-EmployeeUser"],
                   status_code=status.HTTP_200_OK)
async def get_annual_sales():
    """
    not implemented yet .
    """
    pass


@report_router.get("/reports/inventory/out_of_stock", tags=["reports", "-AdminUser", "-EmployeeUser"],
                   status_code=status.HTTP_200_OK)
async def get_inventory_out_of_stock():
    """
    not implemented yet .
    """
    pass


@report_router.get("/reports/inventory/low_stock", tags=["reports", "-AdminUser", "-EmployeeUser"],
                   status_code=status.HTTP_200_OK)
async def get_inventory_low_stock():
    """
    not implemented yet
    """
    pass
