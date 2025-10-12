from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from ..database import get_session
from ..models import User
from ..schemas import Token, UserCreate
from ..auth import get_password_hash, verify_password, create_access_token

# >>> defina o router ANTES dos decorators
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=Token)
def register(payload: UserCreate, session: Session = Depends(get_session)):
    try:
        exists = session.exec(select(User).where(User.username == payload.username)).first()
        if exists:
            raise HTTPException(status_code=409, detail="username already exists")

        user = User(username=payload.username, password_hash=get_password_hash(payload.password))
        session.add(user)
        session.commit()
        session.refresh(user)
        token = create_access_token({"sub": user.username})
        return Token(access_token=token)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="username already exists")

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="invalid credentials")
    token = create_access_token({"sub": user.username})
    return Token(access_token=token)