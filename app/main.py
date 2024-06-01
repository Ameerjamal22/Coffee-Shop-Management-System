from fastapi import FastAPI
from app.apis.OrderApis import order_router
from app.apis.ProductApis import product_router
from app.apis.ReportApis import report_router
from app.apis.CategoryApis import category_router
from app.apis.CustomerApis import customer_router
from app.apis.EmployeeApis import employee_router
from app.apis.OrderItemApis import order_item_router

app: FastAPI = FastAPI()

app.include_router(order_router)
app.include_router(product_router)
app.include_router(report_router)
app.include_router(category_router)
app.include_router(customer_router)
app.include_router(employee_router)
app.include_router(order_item_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
