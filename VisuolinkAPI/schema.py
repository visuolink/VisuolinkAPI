from pydantic import BaseModel, EmailStr, field_serializer
from datetime import datetime
from typing import Optional


class BasiConig(BaseModel):
    class Config:
        from_attributes = True


class GetUsernamesSchema(BaseModel):
    username: str


class GetUserSchema(GetUsernamesSchema):
    name: str
    email: EmailStr
    phone: str


class CreateUserSchema(GetUserSchema):
    password: str


class RequestCredentialSchema(GetUsernamesSchema):
    password: str


class UpdateUserSchema(CreateUserSchema):
    oldUsername: str


class ChangePasswordSchema(RequestCredentialSchema):
    newPassword: str

