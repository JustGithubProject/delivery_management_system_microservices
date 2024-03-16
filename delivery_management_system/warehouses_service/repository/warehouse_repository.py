from warehouses_service.database.database import Session
from warehouses_service.warehouse.models import WareHouse
from warehouses_service.warehouse.custom_exceptions import (
    DeleteWareHouseException
)


class WareHouseRepository:
    def __init__(self):
        self.session = Session()

    def create_warehouse(
        self,
        name,
        location,
        product_name,
        quantity
    ):
        new_warehouse = WareHouse(
            name=name,
            location=location,
            product_name=product_name,
            quantity=quantity
        )
        self.session.add(new_warehouse)
        self.session.commit()

    def get_warehouse_by_name(self, name: str):
        warehouse = self.session.query(WareHouse).filter_by(name=name).first()
        return warehouse

    def get_warehouse_by_id(self, warehouse_id: int):
        warehouse = self.session.query(WareHouse).filter_by(id=warehouse_id).first()
        return warehouse

    def get_warehouses_list(self):
        warehouses = self.session.query(WareHouse).all()
        return warehouses

    def delete_warehouse(self, warehouse_id: int):
        try:
            warehouse = self.get_warehouse_by_id(warehouse_id)
            self.session.delete(warehouse)
        except Exception:
            raise DeleteWareHouseException()


warehouse_repository = WareHouseRepository()
