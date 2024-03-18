from pydantic import BaseModel
from orders_service.order.utils import StatusOrder


class OrderCreate(BaseModel):
    status: StatusOrder
