import logging

from fastapi import FastAPI

from order.routers.Order_router import order_router
from order.routers.OrderItem_router import order_item_router


# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)s - %(asctime)s - %(levelname)s - %(message)s'
)

# An instance of FastAPI (for order service)
order_app = FastAPI()

# Attaching routers to order_app
order_app.include_router(order_router)
order_app.include_router(order_item_router)



