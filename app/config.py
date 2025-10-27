# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl, EmailStr
from typing import Optional

class Settings(BaseSettings):
    # App
    APP_NAME: str = "FastAPI Task Automation"
    ENV: str = "development"
    DEBUG: bool = True
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # Database
    DATABASE_URL: AnyUrl
    # CORS (optional, for frontends)
    CORS_ORIGINS: str = ""

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
