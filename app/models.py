from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relação 1:N (use List[...] do typing)
    sessions: List["GameSession"] = Relationship(back_populates="user")

class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    order: int = Field(index=True)

    options: List["Option"] = Relationship(back_populates="question")

class Option(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="question.id")
    text: str
    is_correct: bool = Field(default=False, index=True)

    question: "Question" = Relationship(back_populates="options")

class GameSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    started_at: datetime = Field(default_factory=datetime.utcnow)
    finished_at: Optional[datetime] = None
    total_score: int = Field(default=0)
    questions_count: int = Field(default=0)

    user: "User" = Relationship(back_populates="sessions")
    answers: List["Answer"] = Relationship(back_populates="session")

class Answer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="gamesession.id")
    question_id: int = Field(foreign_key="question.id")
    option_id: int = Field(foreign_key="option.id")
    is_correct: bool
    elapsed_ms: int
    score_awarded: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

    session: "GameSession" = Relationship(back_populates="answers")