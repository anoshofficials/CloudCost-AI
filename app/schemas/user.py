from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    is_active: bool | None = None
    role: str | None = None
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
