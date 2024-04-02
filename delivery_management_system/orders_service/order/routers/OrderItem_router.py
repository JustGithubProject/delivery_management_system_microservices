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
    ProductFromWarehouseService
)


# Router for OrderItem model
order_item_router = APIRouter()


@order_item_router.post("/order-item/create/")
def order_item_create_handler(data: OrderItemCreate, user: SystemUser = Depends(get_current_user)):
    product = ProductFromWarehouseService.get_product_from_warehouse()
    OrderItemService.create_order_item(data, user, product)