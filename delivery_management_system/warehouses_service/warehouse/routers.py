from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from warehouses_service.warehouse.schemas import (
    WareHouseCreate,
    WareHouseRead
)

from warehouses_service.repository.warehouse_repository import (
    warehouse_repository
)


# Router for warehouse
warehouse_router = APIRouter()


@warehouse_router.post("/create/warehouse/")
def create_warehouse_handler(data: WareHouseCreate):
    pass


