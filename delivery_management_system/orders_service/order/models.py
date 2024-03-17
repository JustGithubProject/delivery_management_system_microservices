from datetime import (
    datetime,
)

from typing import List

from sqlalchemy import Enum
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    relationship,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,

)

from orders_service.order.utils import (
    StatusOrder,
    generate_uuid
)


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "order"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36))
    status: Mapped[StatusOrder] = mapped_column(Enum(StatusOrder), default=StatusOrder.NEW)
    orders_item: Mapped[List["OrderItem"]] = relationship(back_populates="order", uselist=True)


class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    order_id: Mapped[str] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[str] = mapped_column(String(36))
    quantity: Mapped[int] = mapped_column(Integer, default=0)
    order: Mapped["Order"] = relationship(back_populates="orders_item", uselist=False)
