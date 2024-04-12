from fastapi import FastAPI

from warehouse.routers import warehouse_router

# An instance of FastAPI (for warehouse service)
warehouse_app = FastAPI()

# Attaching routers to warehouse_app
warehouse_app.include_router(warehouse_router)

