import logging

from fastapi import FastAPI

from orders_service.order.routers import order_router


# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)s - %(asctime)s - %(levelname)s - %(message)s'
)

order_app = FastAPI()
order_app.include_router(order_router)

