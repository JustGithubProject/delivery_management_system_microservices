from typing import List

from sqlalchemy import Enum
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,
    relationship

)

from delivery.utils import (
    StatusDelivery,
    generate_uuid
)


class Base(DeclarativeBase):
    pass


class DeliveryOrder(Base):
    __tablename__ = "delivery_order"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    order_id: Mapped[str] = mapped_column(String(36))
    delivery_address: Mapped[str] = mapped_column(String)
    status: Mapped[StatusDelivery] = mapped_column(Enum(StatusDelivery), default=StatusDelivery.NEW)