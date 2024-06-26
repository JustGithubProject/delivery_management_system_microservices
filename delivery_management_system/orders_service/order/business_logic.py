import logging

from messaging.consumer import ConsumerProductFromWarehouseService
from messaging.producer import ProducerOrderToDeliveryService
from order.custom_exceptions import (
    OrderCreateException,
    OrderDeleteException,
    OrderItemCreateException,
    OrderItemDeleteException
)
from order.models import Order
from order.schemas import (
    OrderCreate,
    SystemUser,
    OrderItemCreate,

)

from repository.order_repository import (
    order_repository,
    order_item_repository
)


logger = logging.getLogger(__name__)


class OrderService:
    @staticmethod
    def create_order(data: OrderCreate, user: SystemUser) -> Order:
        try:
            order = order_repository.create_order(status=data.status, user_id=user.id)
            return order
        except OrderCreateException as exception:
            logger.error(f"Order create error: {exception}")

    @staticmethod
    def delete_order(order_id: str, user: SystemUser):
        try:
            order_repository.delete_order(order_id=order_id, user_id=user.id)
        except OrderDeleteException as exception:
            logger.error(f"Order delete error: {exception}")


    @staticmethod
    def get_user_orders(user: SystemUser):
        return order_repository.get_list_of_user_orders(user)

    @staticmethod
    def get_user_order(order_id: str, user: SystemUser):
        return order_repository.get_order_by_id(order_id, user)


class OrderDeliveryService:
    @staticmethod
    def send_order_to_delivery(order: Order):
        with ProducerOrderToDeliveryService() as producer_order:
            producer_order.send_order_object(order)


class ProductFromWarehouseService:
    @staticmethod
    def get_product_from_warehouse():
        with ConsumerProductFromWarehouseService() as consumer_product:
            product_obj = consumer_product.receive_product_object_from_warehouse_service()
            return product_obj


class OrderItemService:
    @staticmethod
    def create_order_item(data: OrderItemCreate, user: SystemUser, product):
        try:
            if user:
                order_item_repository.create_order_item(
                    order_id=data.order_id,
                    product_id=product.id,
                    quantity=data.quantity
                )
        except OrderItemCreateException as exception:
            logger.error(f"Order item create error: {exception}")

    @staticmethod
    def get_order_items(order: Order, user: SystemUser):
        return order_item_repository.get_list_of_order_items(order=order, user=user)

    @staticmethod
    def get_order_item(order_item_id: str):
        return order_item_repository.get_order_item_by_id(order_item_id)


    @staticmethod
    def delete_order_item(order_item_id: str, user: SystemUser):
        try:
            order_item_repository.delete_order_item(
                order_item_id=order_item_id,
                user=user
            )
        except OrderItemDeleteException as exception:
            logger.error(f"Order item delete error: {exception}")




