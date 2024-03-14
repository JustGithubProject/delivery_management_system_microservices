from datetime import (
    datetime,
    timedelta
)

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


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    password_hash: Mapped[str]
    sessions: Mapped[List["Session"]] = relationship(back_populates="user")


class Session(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    token: Mapped[str] = mapped_column(String, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow() + timedelta(minutes=30))
    user: Mapped["User"] = relationship(back_populates="sessions")


