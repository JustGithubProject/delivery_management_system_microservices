class DeliveryOrderCreateException(Exception):
    def __init__(self, message="Failed to create delivery_order"):
        self.message = message
        super().__init__(self.message)

