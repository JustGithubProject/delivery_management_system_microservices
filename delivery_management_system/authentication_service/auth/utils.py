import uuid

from typing import (
    Union,
    Any
)

from datetime import (
    datetime,
    timedelta
)

from passlib.context import CryptContext

from auth.constants import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    ALGORITHM
)

from config import (
    JWT_SECRET_KEY,
    JWT_REFRESH_SECRET_KEY
)
from jose import jwt


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_hashed_password(password: str) -> str:
    """The function generates a hashed password using a regular password"""
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """The function verify password and hashed_password"""
    return password_context.verify(password, hashed_password)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """The function generates access_token"""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """The function generates refresh token"""
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def get_default_expires_at():
    return datetime.utcnow() + timedelta(minutes=30)


def generate_uuid():
    """This function will be used instead of a prime number"""
    return str(uuid.uuid4())
