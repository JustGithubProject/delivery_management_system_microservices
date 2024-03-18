from fastapi import (
    APIRouter
)

from delivery_service.messaging.consumer import (
    ConsumerAuthorization
)


delivery_router = APIRouter()


@delivery_router.get("/delivery")
def get_delivery_handler():
    with ConsumerAuthorization() as consumer_auth:
        token, user = consumer_auth.receive_user_obj_and_token_from_auth_service()

