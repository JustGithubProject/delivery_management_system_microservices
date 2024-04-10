from auth.models import User
from database.database import Session
from auth.utils import get_hashed_password
from auth.custom_exceptions import (
    UserCreateException
)


class UserRepository:
    def __init__(self):
        self.session = Session()

    def create_user(
        self,
        username: str,
        email: str,
        password: str
    ):
        try:
            new_user = User(
                username=username,
                email=email,
                password_hash=get_hashed_password(password)
            )
            self.session.add(new_user)
            self.session.commit()
        except Exception:
            raise UserCreateException()

    def get_user_by_email(self, email: str):
        user = self.session.query(User).filter_by(email=email).first()
        return user

    def get_user_by_username(self, username: str):
        user = self.session.query(User).filter_by(username=username).first()
        return user


user_repository = UserRepository()



