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


class SystemUser(BaseModel):
    id: str
    username: str
    email: str
    password_hash: str

    class Config:
        orm_mode = True


class TokenPayload(BaseModel):
    sub: str
    exp: int