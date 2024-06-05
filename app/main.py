from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from app.apis.OrderApis import order_router
from app.apis.ProductApis import product_router
from app.apis.ReportApis import report_router
from app.apis.CategoryApis import category_router
from app.apis.CustomerApis import customer_router
from app.apis.EmployeeApis import employee_router
from app.apis.OrderItemApis import order_item_router
from peewee import IntegrityError

app: FastAPI = FastAPI()

app.include_router(order_router)
app.include_router(product_router)
app.include_router(report_router)
app.include_router(category_router)
app.include_router(customer_router)
app.include_router(employee_router)
app.include_router(order_item_router)


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException) -> JSONResponse:
    """
    handles Http exception raised in the app .
    Args:
        request: the request where the exception happened .
        exc: the exception object .
    Returns:
        (JsonResponse): a json response with the status code and the detail passed to the object constructor .
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


@app.exception_handler(IntegrityError)
async def handle_db_integrity_error(request: Request, exc: IntegrityError) -> JSONResponse:
    """
    handles database integrity errors raised when updating or adding thing to database .
    Args:
        request:the request where the exception happened .
        exc: the exception object
    Returns:
        (JsonResponse): a response with status code 409 (conflict) and a message to describe the cause .
    """
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": f"there was an integrity error in database, {exc.args}"}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
