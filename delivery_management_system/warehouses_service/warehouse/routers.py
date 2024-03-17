import logging

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from warehouses_service.warehouse.custom_exceptions import (
    DeleteWareHouseException,
    CreateWarehouseException,
)

from warehouses_service.warehouse.schemas import (
    WareHouseCreate,
    WareHouseRead
)

from warehouses_service.repository.warehouse_repository import (
    warehouse_repository
)


# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Use a logger for this module
logger = logging.getLogger(__name__)


# Router for warehouse
warehouse_router = APIRouter()


@warehouse_router.post("/warehouse/create/")
def create_warehouse_handler(data: WareHouseCreate):

    # Get warehouse by warehouse_id
    warehouse = warehouse_repository.get_warehouse_by_name(data.name)

    # If the warehouse exists raise HTTPException
    if warehouse:
        logger.warning(f"Attempted to create a warehouse with name that already exists: {data.name}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Warehouse with this name already exists"
        )

    try:
        # Create warehouse using repository for warehouse
        warehouse_repository.create_warehouse(
            name=data.name,
            location=data.location,
            product_name=data.product_name,
            quantity=data.quantity
        )
        logger.info(f"Warehouse created successfully: {data.name}")
    except Exception as ex:
        logger.error(f"Failed to create a new warehouse: {ex}", exc_info=True)
        return f"{ex}: failure to create a new warehouse"


@warehouse_router.get("/warehouse/{warehouse_id}")
def get_warehouse_by_id_handler(warehouse_id: int):
    try:
        # Get warehouse by id that passed from path parameters
        warehouse = warehouse_repository.get_warehouse_by_id(warehouse_id)
        logger.info("Operation was successfully completed")
    except CreateWarehouseException:
        logger.error(f"the warehouse with this ID could not be found", exc_info=True)
        return f"Warehouse with this id does not exist"

    return {"warehouse": warehouse}


@warehouse_router.get("/warehouse/list/")
def get_list_warehouses_handler():
    warehouses = warehouse_repository.get_warehouses_list()
    return warehouses


@warehouse_router.delete("/warehouse/delete/{warehouse_id}")
def delete_warehouse_handler(warehouse_id: int):
    try:
        warehouse_repository.delete_warehouse(warehouse_id)
    except DeleteWareHouseException:
        logger.error("Failed to delete warehouse")
        return "Failed to delete warehouse"
