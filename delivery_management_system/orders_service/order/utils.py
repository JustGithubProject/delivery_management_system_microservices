import enum
import uuid

from datetime import (
    datetime
)


from fastapi import (
    Depends,
    HTTPException,
    status
)
from fastapi.security import OAuth2PasswordBearer

from jose import (
    jwt
)

from pydantic import (
    ValidationError
)

from orders_service.messaging.consumer import (
    ConsumerAuthorization,
)

from orders_service.order.constants import (
    ALGORITHM
)

from orders_service.config import (
    JWT_SECRET_KEY,
    JWT_REFRESH_SECRET_KEY
)
from orders_service.order.schemas import (
    TokenPayload,
    SystemUser
)


class StatusOrder(enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELED = "canceled"


def generate_uuid():
    """This function will be used instead of a prime number"""
    return str(uuid.uuid4())


reusable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def get_current_user(token: str = Depends(reusable_oauth)) -> SystemUser:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    with ConsumerAuthorization() as consumer_auth:
        _, user = consumer_auth.receive_user_obj_and_token_from_auth_service()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return SystemUser(**user)