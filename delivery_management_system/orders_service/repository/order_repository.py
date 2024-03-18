from orders_service.order.models import Order
from orders_service.database.database import Session


class OrderRepository:
    def __init__(self):
        self.session = Session()

    def create_order(
        self,
        user_id,
        status,
    ):
        new_order = Order(user_id=user_id, status=status)
        self.session.add(new_order)
        self.session.commit()


order_repository = OrderRepository()
