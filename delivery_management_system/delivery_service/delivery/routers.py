from fastapi import (
    Depends,
    APIRouter
)

from delivery_service.messaging.consumer import (
    ConsumerAuthorization
)

from delivery_service.delivery.schemas import (
    SystemUser
)

from delivery_service.delivery.utils import (
    get_current_user
)

delivery_router = APIRouter()


@delivery_router.get("/delivery")
def get_delivery_handler(user: SystemUser = Depends(get_current_user)):
    pass

