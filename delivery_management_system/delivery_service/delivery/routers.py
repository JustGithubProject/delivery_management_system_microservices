import logging

from fastapi import (
    Depends,
    APIRouter
)

from messaging.consumer import (
    ConsumerAuthorization,
    ConsumerFromOrderService
)

from delivery.schemas import (
    SystemUser
)

from delivery.utils import (
    get_current_user
)

from repository.deliver_order_repository import (
    delivery_order_repository
)

from delivery.schemas import (
    DeliveryOrderCreate
)

from delivery.custom_exceptions import (
    DeliveryOrderCreateException
)


# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)s - %(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Router for DeliveryOrder model
delivery_router = APIRouter()


@delivery_router.get("/create/delivery")
def create_delivery_order_handler(
        delivery_order: DeliveryOrderCreate,
        user: SystemUser = Depends(get_current_user)
    ):
    with ConsumerFromOrderService() as consumer_order:
        order = consumer_order.receive_order_object()
    try:
        if order.user_id == user.id:
            delivery_order_repository.create_delivery_order(
                order_id=order.id,
                delivery_address=delivery_order.delivery_address
            )
    except DeliveryOrderCreateException as exception:
        logger.error(f"Delivery order create error: {exception}")
        return exception


@delivery_router.get("/get/user/delivery")
def get_delivery_by_order_handler(user: SystemUser = Depends(get_current_user)):
    with ConsumerFromOrderService() as consumer_order:
        order = consumer_order.receive_order_object()
    if order.user_id == user.id:
        delivery = delivery_order_repository.get_delivery_by_order(order)
        return delivery
    else:
        return []




