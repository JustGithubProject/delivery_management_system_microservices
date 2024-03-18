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

from orders_service.order.utils import get_current_user

from orders_service.repository.order_repository import (
    order_repository
)

order_router = APIRouter()


@order_router.post("/order/create/")
def order_create_handler(data: OrderCreate, user: SystemUser = Depends(get_current_user)):
    order_repository.create_order(status=data.status, user_id=user.id)
