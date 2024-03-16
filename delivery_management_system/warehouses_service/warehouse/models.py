from typing import List

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


class Base(DeclarativeBase):
    pass


class WareHouse(Base):
    __tablename__ = "warehouses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    location: Mapped[str] = mapped_column(String(100))
    product_name: Mapped[str] = mapped_column(String(100))
    quantity: Mapped[int] = mapped_column(default=0)
