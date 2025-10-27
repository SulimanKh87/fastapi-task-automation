"""Database models for the application (Tasks + Users)."""
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Task(Base):
    """
    Represents a task item created by the user.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)


class User(Base):
    """
    Represents an authenticated user in the system.
    Each user has a unique username and email.
    The hashed password is stored securely using bcrypt.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
