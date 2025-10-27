# app/routers/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, models
from ..deps import get_current_user
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=schemas.UserOut)
def read_me(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return current_user
