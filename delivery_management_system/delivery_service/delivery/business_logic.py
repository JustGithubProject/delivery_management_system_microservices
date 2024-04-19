from repository.deliver_order_repository import delivery_order_repository


class DeliveryOrderService:
    @staticmethod
    def create_delivery_order(
        order_id: str,
        delivery_address: str,
    ):
        delivery_order_repository.create_delivery_order(
            order_id,
            delivery_address
        )

    @staticmethod
    def get_delivery_by_order(order_id):
        delivery_order_repository.get_delivery_by_order(order_id)

