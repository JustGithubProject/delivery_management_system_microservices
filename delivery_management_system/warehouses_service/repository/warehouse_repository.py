from database.database import Session


class WareHouseRepository:
    def __init__(self):
        self.session = Session()

    def create_warehouse(
        self,
        name,
        location,
        quantity
    ):
        ...