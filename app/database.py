from __future__ import annotations
from sqlmodel import Session, SQLModel, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./speedrun.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)

def init_db() -> None:
    # importa modelos para registrar as tabelas
    from . import models  # noqa: F401
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    with Session(engine) as session:
        yield session