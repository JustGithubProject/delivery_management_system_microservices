from fastapi import (
    Depends,
    APIRouter
)

from delivery_service.messaging.consumer import (
    ConsumerAuthorization,
    ConsumerFromOrderService
)

from delivery_service.delivery.schemas import (
    SystemUser
)

from delivery_service.delivery.utils import (
    get_current_user
)

from delivery_service.repository.deliver_order_repository import (
    delivery_order_repository
)

from delivery_service.delivery.schemas import (
    DeliveryOrderCreate
)

from delivery_service.delivery.custom_exceptions import (
    DeliveryOrderCreateException
)

delivery_router = APIRouter()


@delivery_router.get("/create/delivery")
def create_delivery_order_handler(
        delivery_order: DeliveryOrderCreate,
        user: SystemUser = Depends(get_current_user)
    ):
    try:
        with ConsumerFromOrderService() as consumer_order:
            order = consumer_order.receive_order_object()

        if order.user_id == user.id:
            delivery_order_repository.create_delivery_order(
                order_id=delivery_order.order_id,
                delivery_address=delivery_order.delivery_address
            )
    except DeliveryOrderCreateException as exception:
        return exception


