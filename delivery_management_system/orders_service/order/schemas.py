import enum
from typing import Optional

from pydantic import BaseModel


class StatusOrder(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELED = "canceled"


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

