from database.database import (
    Session
)
from delivery.custom_exceptions import (
    DeliveryOrderCreateException
)

from delivery.models import (
    DeliveryOrder
)


class DeliveryOrderRepository:
    def __init__(self):
        self.session = Session()

    def create_delivery_order(
        self,
        order_id: str,
        delivery_address: str,
    ):
        try:
            delivery_order = DeliveryOrder(
                order_id=order_id,
                delivery_address=delivery_address
            )
            self.session.add(delivery_order)
            self.session.commit()
        except Exception:
            raise DeliveryOrderCreateException()

    def get_delivery_by_order(self, order_id):
        return self.session.query(DeliveryOrder).filter_by(order_id=order_id).first()


delivery_order_repository = DeliveryOrderRepository()