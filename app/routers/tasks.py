# app/routers/tasks.py
"""Router for managing tasks in the task management application."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db
from app.security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[schemas.Task])
def read_tasks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Return all tasks owned by the authenticated user."""
    return crud.list_tasks_by_user(db, user_id=current_user.id)

@router.post("/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Create a new task linked to the authenticated user."""
    return crud.create_task_for_user(db, payload=task, user_id=current_user.id)

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Return a single task ONLY if it belongs to the authenticated user."""
    task = crud.get_task_by_id_and_user(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    payload: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Update a task ONLY if owned by the authenticated user."""
    task = crud.update_task_for_user(db, task_id, current_user.id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Delete a task ONLY if owned by the authenticated user."""
    success = crud.delete_task_for_user(db, task_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

    return
