from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from typing import List

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    username: str
    password: str

class QuestionOut(BaseModel):
    id: int
    text: str
    options: List[dict]

class LaunchResponse(BaseModel):
    session_id: int
    questions: List[QuestionOut]

class AnswerIn(BaseModel):
    session_id: int
    question_id: int
    option_id: int
    elapsed_ms: int

class AnswerOut(BaseModel):
    correct: bool
    score_awarded: int
    total_score: int

class ScoreOut(BaseModel):
    session_id: int
    finished_at: datetime
    total_score: int
    answers: List[dict]