from typing import List

from sqlalchemy import (
    String,
    Integer,
    Numeric,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,
    relationship
)

from warehouse.utils import (
    generate_uuid
)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    product_name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    warehouses: Mapped[List["WareHouse"]] = relationship(back_populates="product", uselist=True)


class WareHouse(Base):
    __tablename__ = "warehouse"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    name: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(100))
    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(default=0)
    product: Mapped["Product"] = relationship(back_populates="warehouses", uselist=False)
