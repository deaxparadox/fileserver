from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserRequestSchema(BaseModel):
    username: str
    password: str
    email: EmailStr