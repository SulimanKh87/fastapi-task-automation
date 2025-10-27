""" Pydantic models for task management application. """
from pydantic import BaseModel, EmailStr, field_validator

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True

# ----- Users -----
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def strong_password(cls, v: str) -> str:
        # Simple baseline: length check; improve later with zxcvbn, etc.
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return v

class UserOut(UserBase):
    id: int
    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2

# ----- Auth / Token -----
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: str | None = None  # subject (we use email)