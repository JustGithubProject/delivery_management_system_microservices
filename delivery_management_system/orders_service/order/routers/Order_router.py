import logging

from fastapi import (
    APIRouter,
    Depends
)

from orders_service.order.schemas import (
    OrderCreate,
    SystemUser,
    OrderItemCreate
)

from orders_service.order.custom_exceptions import (
    OrderCreateException,
    OrderDeleteException,
    OrderItemCreateException,
    OrderItemDeleteException
)

from orders_service.messaging.producer import (
    ProducerOrderToDeliveryService
)

from orders_service.order.utils import get_current_user
from orders_service.repository.order_repository import order_repository

from orders_service.order.business_logic import (
    OrderService,
    DeliveryService
)


# Router for Order model
order_router = APIRouter()

##############################################################
# Handlers for Order model that can use only current_user    #
##############################################################


@order_router.post("/order/create/")
def order_create_handler(data: OrderCreate, user: SystemUser = Depends(get_current_user)):
    order = OrderService.create_order(data, user)
    DeliveryService.send_order_to_delivery(order)
    return {"message": "Order created successfully and sent to delivery"}


@order_router.delete("/order/delete/{order_id}")
def delete_order_handler(order_id: str, user: SystemUser = Depends(get_current_user)):
    OrderService.delete_order(order_id, user)
    return {"message": "Order deleted successfully"}


@order_router.get("/order/list-of-user-orders/")
def order_list_handler(user: SystemUser = Depends(get_current_user)):
    return OrderService.get_user_orders(user)
