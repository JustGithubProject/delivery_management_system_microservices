from repository.user_repository import user_repository

from auth.schemas import UserAuth
from auth.custom_exceptions import UserCreateException


class UserService:
    @staticmethod
    def register_user(data: UserAuth):
        try:
            user_repository.create_user(
                username=data.username,
                email=data.email,
                password=data.password
            )
        except UserCreateException as ex:
            return f"{ex}: failure to create new user"

    @staticmethod
    def get_user_by_username(username: str):
        return user_repository.get_user_by_email(username)

    @staticmethod
    def list_users():
        return user_repository.get_list_of_users()