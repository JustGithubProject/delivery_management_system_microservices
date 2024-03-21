from orders_service.order.models import Order
from orders_service.database.database import Session

from orders_service.order.custom_exceptions import (
    OrderCreateException,
    OrderDeleteException
)


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

    def get_order_by_id(self, order_id: str, user_id: str):
        order = self.session.query(Order).filter_by(id=order_id, user_id=user_id).first()
        return order

    def delete_order(self, order_id: str, user_id: str):
        try:
            order = self.get_order_by_id(order_id, user_id)
            self.session.delete(order)
        except Exception:
            raise OrderDeleteException()


order_repository = OrderRepository()
