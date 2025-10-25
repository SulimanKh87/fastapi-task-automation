""" CRUD operations for Task model. """
from sqlalchemy.orm import Session
from app import models, schemas

def list_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, payload: schemas.TaskCreate):
    task = models.Task(title=payload.title, description=payload.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
