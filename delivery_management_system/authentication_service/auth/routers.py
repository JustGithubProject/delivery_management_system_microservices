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

from schemas import (
    UserOut,
    UserAuth
)


user_router = APIRouter()

@user_router.post("/signup", summary="Create new user", response_model=UserOut)
def create_user_handler(data: UserAuth):
    user =