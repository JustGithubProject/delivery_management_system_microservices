from order.models import (
    Order,
    OrderItem
)

from database.database import Session

from order.custom_exceptions import (
    OrderCreateException,
    OrderDeleteException,
    OrderItemCreateException,
    OrderItemDeleteException
)
from order.schemas import SystemUser


class OrderRepository:
    def __init__(self):
        self.session = Session()

    def create_order(
        self,
        user_id,
        status,
    ):
        try:
            new_order = Order(user_id=user_id, status=status)
            self.session.add(new_order)
            self.session.commit()
            return new_order

        except Exception:
            raise OrderCreateException()

    def get_list_of_user_orders(self, user):
        orders = self.session.query(Order).filter_by(user_id=user.id).all()
        return orders

    def get_order_by_id(self, order_id: str, user: SystemUser):
        order = self.session.query(Order).filter_by(id=order_id, user_id=user.id).first()
        return order

    def delete_order(self, order_id: str, user_id: str):
        try:
            order = self.get_order_by_id(order_id, user_id)
            self.session.delete(order)
        except Exception:
            raise OrderDeleteException()


class OrderItemRepository:
    def __init__(self):
        self.session = Session()

    def create_order_item(
        self,
        order_id,
        product_id,
        quantity
    ):
        try:
            order_item = OrderItem(
                order_id=order_id,
                product_id=product_id,
                quantity=quantity
            )
            self.session.add(order_item)
            self.session.commit()
            return order_item
        except Exception:
            raise OrderItemCreateException()

    def get_list_of_order_items(self, order, user):
        if user.id == order.user_id:
            order_items = self.session.query(OrderItem).filter_by(order_id=order.id).all()
            return order_items
        else:
            return []

    def get_order_item_by_id(self, order_item_id):
        order_item = self.session.query(OrderItem).filter_by(id=order_item_id).first()
        return order_item

    def delete_order_item(self, order_item_id, user):
        try:
            order_item = self.get_order_item_by_id(order_item_id)
            if order_item.order.user_id == user.id:
                self.session.delete(order_item)
        except Exception:
            raise OrderItemDeleteException()


order_repository = OrderRepository()
order_item_repository = OrderItemRepository()

