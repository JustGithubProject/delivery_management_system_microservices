from typing import Optional

from pydantic import BaseModel
from orders_service.order.utils import StatusOrder


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