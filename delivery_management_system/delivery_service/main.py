from fastapi import FastAPI

from delivery.routers import delivery_router

# An instance of FastAPI (for delivery service)
delivery_app = FastAPI()

# Attaching routers to delivery_app
delivery_app.include_router(delivery_router)

