from fastapi import FastAPI

from warehouse.routers import warehouse_router


warehouse_app = FastAPI()

warehouse_app.include_router(warehouse_router)

