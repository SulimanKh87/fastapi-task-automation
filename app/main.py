"""Main FastAPI application entry point with authentication, user, and task routes."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import auth, users, tasks

# ⚠️ Do NOT use Base.metadata.create_all(bind=engine) in production
# Alembic handles migrations and schema creation
# (keep this commented out unless running standalone local tests)
# from app.database import Base, engine
# Base.metadata.create_all(bind=engine)

# -------------------------------------------------------------------
# Initialize FastAPI app
# -------------------------------------------------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version="0.4.0",
    description="FastAPI backend with JWT authentication, Alembic migrations, and PostgreSQL",
)

# -------------------------------------------------------------------
# Configure CORS
# -------------------------------------------------------------------
# Read comma-separated origins from .env (CORS_ORIGINS=http://localhost:3000,...)
origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]

if origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# -------------------------------------------------------------------
# Include Routers
# -------------------------------------------------------------------
# Routers grouped by domain:
# - /auth → signup/login
# - /users → protected routes (JWT required)
# - /tasks → your CRUD endpoints
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

# -------------------------------------------------------------------
# Health Check Endpoints
# -------------------------------------------------------------------
@app.get("/", tags=["Root"])
def root():
    """Root route to verify API connection."""
    return {"message": f"{settings.APP_NAME} is running and connected to the database."}


@app.get("/health", tags=["Health"])
def health_check():
    """Lightweight healthcheck endpoint for Docker and uptime monitors."""
    return {"status": "healthy"}
