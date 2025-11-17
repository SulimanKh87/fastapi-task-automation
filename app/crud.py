# app/crud.py
"""CRUD operations for Task model with user ownership enforcement."""
from sqlalchemy.orm import Session
from app import models, schemas


# ---------------------------
# READ
# ---------------------------
def list_tasks_by_user(db: Session, user_id: int):
    """Return only tasks owned by the given user."""
    return (
        db.query(models.Task)
        .filter(models.Task.owner_id == user_id)
        .all()
    )


def get_task_by_id_and_user(db: Session, task_id: int, user_id: int):
    """Return a task only if it belongs to the authenticated user."""
    return (
        db.query(models.Task)
        .filter(
            models.Task.id == task_id,
            models.Task.owner_id == user_id
        )
        .first()
    )


# ---------------------------
# CREATE
# ---------------------------
def create_task_for_user(db: Session, payload: schemas.TaskCreate, user_id: int):
    """Create a new task owned by the authenticated user."""
    task = models.Task(
        title=payload.title,
        description=payload.description,
        owner_id=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


# ---------------------------
# UPDATE
# ---------------------------
def update_task_for_user(db: Session, task_id: int, user_id: int, payload: schemas.TaskCreate):
    """Update a user's own task."""
    task = get_task_by_id_and_user(db, task_id, user_id)
    if not task:
        return None

    task.title = payload.title
    task.description = payload.description
    db.commit()
    db.refresh(task)
    return task


# ---------------------------
# DELETE
# ---------------------------
def delete_task_for_user(db: Session, task_id: int, user_id: int):
    """Delete a task only if it belongs to the user."""
    task = get_task_by_id_and_user(db, task_id, user_id)
    if not task:
        return False

    db.delete(task)
    db.commit()
    return True
