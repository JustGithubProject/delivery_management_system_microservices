from fastapi import (
    APIRouter,
    Depends
)

from orders_service.order.schemas import (
    OrderCreate,
    SystemUser
)

from orders_service.messaging.consumer import (
    ConsumerAuthorization
)

from orders_service.order.custom_exceptions import (
    OrderCreateException,
    OrderDeleteException
)

from orders_service.order.utils import get_current_user

from orders_service.repository.order_repository import (
    order_repository
)

order_router = APIRouter()


@order_router.post("/order/create/")
def order_create_handler(data: OrderCreate, user: SystemUser = Depends(get_current_user)):
    try:
        order_repository.create_order(status=data.status, user_id=user.id)
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





