from fastapi import FastAPI

from warehouses_service.warehouse.routers import warehouse_router


warehouse_app = FastAPI()

warehouse_app.include_router(warehouse_router)

