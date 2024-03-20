from delivery_service.database.database import (
    Session
)
from delivery_service.delivery.custom_exceptions import (
    DeliveryOrderCreateException
)

from delivery_service.delivery.models import (
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


delivery_order_repository = DeliveryOrderRepository()