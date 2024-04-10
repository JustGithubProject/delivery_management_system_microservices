from fastapi import FastAPI

from delivery.routers import delivery_router


delivery_app = FastAPI()
delivery_app.include_router(delivery_router)
