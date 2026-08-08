"""
Application Configuration

Uses pydantic-settings to load environment variables from .env file.

TODO:
- Create a Settings class that extends BaseSettings
- Define all config fields with types and defaults:
    - DATABASE_URL: str
    - REDIS_URL: str
    - SECRET_KEY: str
    - ALGORITHM: str = "HS256"
    - ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    - ANTHROPIC_API_KEY: str | None = None
    - OPENAI_API_KEY: str | None = None
    - SEC_USER_AGENT: str
- Configure model_config to read from .env file
- Create a cached `get_settings()` function using @lru_cache
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, ConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # --- Required fields (app won't start without these) ---
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ANTHROPIC_API_KEY: str | None = None
    OPENAI_API_KEY : str | None = None
    SEC_USER_AGENT: str
    model_config = ConfigDict(env_file =".env")
    


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
