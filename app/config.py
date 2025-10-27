# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl

class Settings(BaseSettings):
    # ─── App ─────────────────────────────
    APP_NAME: str = "FastAPI Task Automation"
    ENV: str = "development"
    DEBUG: bool = True

    # ─── Security ────────────────────────
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ─── Database ────────────────────────
    DATABASE_URL: AnyUrl

    # ─── CORS ────────────────────────────
    CORS_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"

    # ✅ ignore extra env vars (from Docker or pgAdmin)
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )

settings = Settings()
