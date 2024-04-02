import logging

from fastapi import (
    APIRouter,
    Depends
)

from orders_service.order.schemas import (
    OrderItemCreate,
    SystemUser
)

from orders_service.order.utils import get_current_user
from orders_service.order.business_logic import (
    OrderItemService,
    OrderService,
    ProductFromWarehouseService
)


# Router for OrderItem model
order_item_router = APIRouter()


@order_item_router.post("/order-item/create/")
def order_item_create_handler(data: OrderItemCreate, user: SystemUser = Depends(get_current_user)):
    product = ProductFromWarehouseService.get_product_from_warehouse()
    OrderItemService.create_order_item(data, user, product)


@order_item_router.get("/order-items/get/{order_id}")
def list_order_items_of_current_user_handler(order_id, user: SystemUser = Depends(get_current_user)):
    order = OrderService.get_user_order(order_id, user)
    order_items = OrderItemService.get_order_items(order, user)
    return order_items
