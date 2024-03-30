from fastapi import (
    APIRouter,
    Depends
)

from orders_service.order.schemas import (
    OrderCreate,
    SystemUser,
    OrderItemCreate
)

from orders_service.messaging.consumer import (
    ConsumerAuthorization,
    ConsumerProductFromWarehouseService
)

from orders_service.messaging.producer import (
    ProducerOrderToDeliveryService
)

from orders_service.order.custom_exceptions import (
    OrderCreateException,
    OrderDeleteException,
    OrderItemCreateException,
    OrderItemDeleteException
)
from orders_service.order.utils import get_current_user

from orders_service.repository.order_repository import (
    order_repository,
    order_item_repository
)

# Router for Order model
order_router = APIRouter()


@order_router.post("/order/create/")
def order_create_handler(data: OrderCreate, user: SystemUser = Depends(get_current_user)):
    try:
        order = order_repository.create_order(status=data.status, user_id=user.id)
        with ProducerOrderToDeliveryService() as producer_order:
            producer_order.send_order_object(order)
    except OrderCreateException as exception:
        return exception


@order_router.get("/order/list-of-user-orders/")
def order_list_handler(user: SystemUser = Depends(get_current_user)):
    return order_repository.get_list_of_user_orders(user)


@order_router.delete("/order/delete/")
def delete_order_handler(order_id: str, user: SystemUser = Depends(get_current_user)):
    try:
        order_repository.delete_order(order_id=order_id, user_id=user.id)
    except OrderDeleteException as exception:
        return exception

######################################################################


# Router for OrderItem model
order_item_router = APIRouter()


@order_item_router.post("/order-item/create/")
def order_item_create_handler(data: OrderItemCreate, user: SystemUser = Depends(get_current_user)):
    try:
        with ConsumerProductFromWarehouseService() as consumer_product:
            product_obj = consumer_product.receive_product_object_from_warehouse_service()
            order_item_repository.create_order_item(
                order_id=data.order_id,
                product_id=product_obj.id,
                quantity=data.quantity
            )
    except OrderItemCreateException as exception:
        return exception


@order_item_router.delete("/order-item/delete/{order_item_id}")
def order_item_delete_handler(order_item_id: str, user: SystemUser = Depends(get_current_user)):
    try:
        order_item_repository.delete_order_item(
            order_item_id=order_item_id,
            user=user
        )
    except OrderItemDeleteException as exception:
        return exception



