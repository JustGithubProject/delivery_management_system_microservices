class OrderCreateException(Exception):
    def __init__(self, message="Failed to create order"):
        self.message = message
        super().__init__(self.message)


class OrderDeleteException(Exception):
    def __init__(self, message="Failed to delete order"):
        self.message = message
        super().__init__(self.message)

