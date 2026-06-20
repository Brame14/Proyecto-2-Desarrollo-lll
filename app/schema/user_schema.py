from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    role: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str
    password: str
    role: str


class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str
    password: str