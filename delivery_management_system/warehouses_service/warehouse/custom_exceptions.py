class DeleteWareHouseException(Exception):
    """Custom Exception for delete warehouse"""
    def __init__(self, message="Failed to delete warehouse"):
        self.message = message
        super().__init__(self.message)


