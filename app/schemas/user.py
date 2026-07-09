from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# -----------------------------
# Base Schema
# -----------------------------
class UserBase(BaseModel):
    full_name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    email: EmailStr


# -----------------------------
# Register User
# -----------------------------
class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )


# -----------------------------
# Login User
# -----------------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# -----------------------------
# User Response
# -----------------------------
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# -----------------------------
# JWT Token
# -----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


# -----------------------------
# JWT Payload
# -----------------------------
class TokenData(BaseModel):
    sub: str | None = None