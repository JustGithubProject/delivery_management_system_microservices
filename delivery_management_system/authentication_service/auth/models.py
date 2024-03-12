from sqlalchemy import (
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,

)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    password_hash: Mapped[str]



