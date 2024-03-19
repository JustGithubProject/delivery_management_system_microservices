from pydantic import BaseModel


class SystemUser(BaseModel):
    id: str
    username: str
    email: str
    password_hash: str

    class Config:
        orm_mode = True


class TokenPayload(BaseModel):
    sub: str
    exp: int
