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

from authentication_service.auth.utils import (
    get_default_expires_at,
    generate_uuid
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    password_hash: Mapped[str] = mapped_column(String)
    sessions: Mapped[List["Session"]] = relationship(back_populates="user", uselist=True)


class Session(Base):
    __tablename__ = "session"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    token: Mapped[str] = mapped_column(String, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, default=get_default_expires_at)
    user: Mapped["User"] = relationship(back_populates="sessions", uselist=False)


