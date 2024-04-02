import logging

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


# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)s - %(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

######################################################################






@order_item_router.get("/order-item/get/{order_item_id}")
def order_item_handler(order_item_id):
    order_item = order_item_repository.get_order_item_by_id(order_item_id)
    return order_item


@order_item_router.delete("/order-item/delete/{order_item_id}")
def order_item_of_current_user_delete_handler(order_item_id: str, user: SystemUser = Depends(get_current_user)):
    try:
        order_item_repository.delete_order_item(
            order_item_id=order_item_id,
            user=user
        )
    except OrderItemDeleteException as exception:
        logger.error(f"Order item delete error: {exception}")
        return exception


