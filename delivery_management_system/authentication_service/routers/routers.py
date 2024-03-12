from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from fastapi.responses import RedirectResponse

from authentication_service.auth.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)


user_router = APIRouter()