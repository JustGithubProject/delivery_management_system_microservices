class DeleteWareHouseException(Exception):
    """Custom Exception for delete warehouse"""
    def __init__(self, message="Failed to delete warehouse"):
        self.message = message
        super().__init__(self.message)


class CreateWarehouseException(Exception):
    """Custom Exception for create warehouse"""
    def __init__(self, message="Failed to create warehouse"):
        self.message = message
        super().__init__(self.message)