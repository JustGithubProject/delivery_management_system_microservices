import logging

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from fastapi.responses import RedirectResponse

from authentication_service.auth.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)

from authentication_service.auth.schemas import (
    UserOut,
    UserAuth
)

from authentication_service.repository.user_repository import user_repository

from authentication_service.messaging.producer import (
    ProducerAuthorization
)

from authentication_service.auth.custom_exceptions import (
    UserCreateException
)


# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)s - %(asctime)s - %(levelname)s - %(message)s'
)

# Use a logger for this module
logger = logging.getLogger(__name__)

user_router = APIRouter()


@user_router.post("/auth/signup", summary="Create new user", response_model=UserOut)
def create_user_handler(data: UserAuth):

    # Get user by email
    user = user_repository.get_user_by_email(data.email)

    # If the user exists raise HTTPException
    if user:
        logger.warning(f"Attempted to create a user with an email that already exists: {data.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    try:
        # Create user using repository for user
        user_repository.create_user(
            username=data.username,
            email=data.email,
            password=data.password
        )
        logger.info(f"User created successfully: {data.username}")
    except UserCreateException as ex:
        logger.error(f"Failed to create a new user: {ex}", exc_info=True)
        return f"{ex}: failure to create new user"


@user_router.post("/auth/login", summary="Create access and refresh tokens for user")
def login_handler(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"Login attempt with username: {form_data.username}")

    # Get user by username
    user = user_repository.get_user_by_username(form_data.username)

    # If the user doesn't exist raise an HTTPException
    if not user:
        logger.warning(f"Login attempt failed. User with username '{form_data.username}' not found.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    # If the password does not match the encrypted password raise and HTTPException
    if not verify_password(form_data.password, user.password_hash):
        logger.warning(f"Login attempt failed. Incorrect password for user '{form_data.username}'.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    # Create access and refresh token using email
    access_token = create_access_token(user.email)
    refresh_token = create_refresh_token(user.email)

    with ProducerAuthorization() as producer_auth:
        producer_auth.send_user_object_and_token_to_services(access_token, user)

    logger.info(f"User '{form_data.username}' successfully logged in.")

    # Return access and refresh token
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


