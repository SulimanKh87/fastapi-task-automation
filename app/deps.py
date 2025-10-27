# app/deps.py
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError
from .security import oauth2_scheme, decode_token
from .database import get_db
from . import models

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> models.User:
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exc
    except JWTError:
        raise credentials_exc

    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise credentials_exc
    return user
