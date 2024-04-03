import logging

from fastapi import (
    APIRouter,
    Depends
)

from ...order.schemas import (
    OrderCreate,
    SystemUser
)


from ...order.utils import get_current_user


from ...order.business_logic import (
    OrderService,
    OrderDeliveryService
)


# Router for Order model
order_router = APIRouter()

##############################################################
# Handlers for Order model that can use only current_user    #
##############################################################


@order_router.post("/order/create/")
def order_create_handler(data: OrderCreate, user: SystemUser = Depends(get_current_user)):
    order = OrderService.create_order(data, user)
    OrderDeliveryService.send_order_to_delivery(order)
    return {"message": "Order created successfully and sent to delivery"}


@order_router.delete("/order/delete/{order_id}")
def delete_order_handler(order_id: str, user: SystemUser = Depends(get_current_user)):
    OrderService.delete_order(order_id, user)
    return {"message": "Order deleted successfully"}


@order_router.get("/order/list-of-user-orders/")
def order_list_handler(user: SystemUser = Depends(get_current_user)):
    return OrderService.get_user_orders(user)


@order_router.get("/order-user/{order_id}")
def order_by_id_handler(order_id: str, user: SystemUser = Depends(get_current_user)):
    return OrderService.get_user_order(order_id, user)

