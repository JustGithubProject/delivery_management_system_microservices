from fastapi import APIRouter

from orders_service.order.schemas import (
    OrderCreate
)

from orders_service.messaging.consumer import (
    ConsumerAuthorization
)

from orders_service.repository.order_repository import (
    order_repository
)

order_router = APIRouter()


@order_router.post("/order/create/")
def order_create_handler(data: OrderCreate):
    with ConsumerAuthorization() as consumer_auth:
        token, user = consumer_auth.receive_user_obj_and_token_from_auth_service()
    order_repository.create_order(status=data.status, user_id=user.id)
