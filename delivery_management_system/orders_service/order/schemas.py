from typing import Optional

from pydantic import BaseModel
from ..order.utils import StatusOrder


class OrderCreate(BaseModel):
    status: StatusOrder


class TokenPayload(BaseModel):
    sub: str
    exp: int


class SystemUser(BaseModel):
    id: str
    username: str
    email: str
    password_hash: str

    class Config:
        orm_mode = True


class OrderItemCreate(BaseModel):
    order_id: str
    # product_id: str
    quantity: int

