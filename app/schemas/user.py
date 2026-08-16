from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
