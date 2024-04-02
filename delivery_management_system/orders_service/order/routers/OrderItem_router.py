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
    return {"message": "OrderItem created successfully and sent to delivery"}


@order_item_router.get("/order-items/get/{order_id}")
def list_order_items_of_current_user_handler(order_id, user: SystemUser = Depends(get_current_user)):
    order = OrderService.get_user_order(order_id, user)
    order_items = OrderItemService.get_order_items(order, user)
    return order_items


@order_item_router.get("/order-item/get/{order_item_id}")
def order_item_handler(order_item_id: str):
    order_item = OrderItemService.get_order_item(order_item_id)
    return order_item


@order_item_router.delete("/order-item/delete/{order_item_id}")
def order_item_of_current_user_delete_handler(order_item_id: str, user: SystemUser = Depends(get_current_user)):
    OrderItemService.delete_order_item(order_item_id, user)
    return {"message": "OrderItem deleted successfully"}


