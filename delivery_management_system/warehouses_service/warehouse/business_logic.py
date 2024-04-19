from repository.warehouse_repository warehouse_repository



class WareHouseService:
    @staticmethod
    def create_warehouse(
        name,
        location,
        product_name,
        quantity
    ):
        warehouse_repository.create_warehouse(
            name=name,
            location=location,
            product_name=product_name,
            quantity=quantity
        )

    @staticmethod
    def get_warehouse_by_name(name: str):
        return warehouse_repository.get_warehouse_by_name(name)

    @staticmethod
    def get_warehouse_by_id(warehouse_id: int):
        return warehouse_repository.get_warehouse_by_id(warehouse_id)


    @staticmethod
    def get_warehouses_list():
        return warehouse_repository.get_warehouses_list()

    @staticmethod
    def delete_warehouse(warehouse_id: int):
        warehouse_repository.delete_warehouse(warehouse_id)