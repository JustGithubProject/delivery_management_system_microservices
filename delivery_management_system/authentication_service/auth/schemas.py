from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str


class UserAuth(BaseModel):
    username: str
    email: str
    password: str