# app/crud.py
"""CRUD operations for Task model."""
from sqlalchemy.orm import Session
from app import models, schemas

def list_tasks_by_user(db: Session, user_id: int):
    """Return only tasks owned by the given user."""
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

def create_task_for_user(db: Session, payload: schemas.TaskCreate, user_id: int):
    """Create a new task linked to the authenticated user."""
    task = models.Task(
        title=payload.title,
        description=payload.description,
        owner_id=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
