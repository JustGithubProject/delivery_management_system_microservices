from authentication_service.models.models import User
from authentication_service.database.database import Session
from authentication_service.auth.utils import get_hashed_password


class UserRepository:
    def __init__(self):
        self.session = Session()

    def create_user(
        self,
        username: str,
        email: str,
        password: str
    ):
        new_user = User(
            username=username,
            email=email,
            password_hash=get_hashed_password(password)
        )
        self.session.add(new_user)
        self.session.commit()





