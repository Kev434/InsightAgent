"""
User Schemas (Pydantic)

Request/response models for user-related endpoints.

TODO:
- UserCreate: email (EmailStr), password (str, min_length=8), full_name (str | None)
- UserLogin: email (EmailStr), password (str)
- UserResponse: id (UUID), email, full_name, is_active, created_at
    - Use model_config = ConfigDict(from_attributes=True) for ORM compatibility
- TokenResponse: access_token (str), token_type (str) = "bearer"
"""

from pydantic import BaseModel


class UserCreate(BaseModel):
    """Schema for user registration request."""
    pass


class UserLogin(BaseModel):
    """Schema for user login request."""
    pass


class UserResponse(BaseModel):
    """Schema for user data in API responses."""
    pass


class TokenResponse(BaseModel):
    """Schema for JWT token response after login."""
    pass
