from fastapi import FastAPI

from orders_service.order.routers import order_router


order_app = FastAPI()
order_app.include_router(order_router)

