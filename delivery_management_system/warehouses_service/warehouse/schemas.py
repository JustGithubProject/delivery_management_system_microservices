from pydantic import BaseModel


class BaseWareHouse(BaseModel):
    name: str
    location: str
    product_name: str
    quantity: int


class WareHouseCreate(BaseWareHouse):
    pass


class WareHouseRead(BaseWareHouse):
    id: int
