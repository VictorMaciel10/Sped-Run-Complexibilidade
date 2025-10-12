from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import get_session
from ..models import Question, Option, GameSession, Answer
from ..schemas import LaunchResponse, QuestionOut, AnswerIn, AnswerOut, ScoreOut
from ..auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/game", tags=["game"])

def calc_score(elapsed_ms: int) -> int:
    base = 1000 - (elapsed_ms // 100)
    return max(int(base), 100)

@router.post("/launch", response_model=LaunchResponse)
def launch(session_db: Session = Depends(get_session), user=Depends(get_current_user)):
    gs = GameSession(user_id=user.id)
    session_db.add(gs)
    session_db.commit()
    session_db.refresh(gs)

    questions = session_db.exec(select(Question).order_by(Question.order)).all()
    q_out: list[QuestionOut] = []
    for q in questions:
        opts = session_db.exec(select(Option).where(Option.question_id == q.id)).all()
        q_out.append(QuestionOut(id=q.id, text=q.text,
                   options=[{"id": o.id, "text": o.text} for o in opts]))
    return LaunchResponse(session_id=gs.id, questions=q_out)

@router.post("/answer", response_model=AnswerOut)
def answer(payload: AnswerIn, session_db: Session = Depends(get_session),
           user=Depends(get_current_user)):
    gs = session_db.get(GameSession, payload.session_id)
    if not gs or gs.user_id != user.id:
        raise HTTPException(status_code=404, detail="session not found")

    question = session_db.get(Question, payload.question_id)
    option = session_db.get(Option, payload.option_id)
    if not question or not option or option.question_id != question.id:
        raise HTTPException(status_code=400, detail="invalid question/option")

    correct_opt = session_db.exec(
        select(Option).where(Option.question_id == question.id, Option.is_correct == True)
    ).first()
    is_correct = (option.id == correct_opt.id)

    score_awarded = calc_score(payload.elapsed_ms) if is_correct else 0
    ans = Answer(
        session_id=gs.id,
        question_id=question.id,
        option_id=option.id,
        is_correct=is_correct,
        elapsed_ms=payload.elapsed_ms,
        score_awarded=score_awarded,
    )
    session_db.add(ans)
    if is_correct:
        gs.total_score += score_awarded
        gs.questions_count += 1
    session_db.commit()

    return AnswerOut(correct=is_correct, score_awarded=score_awarded,
                     total_score=gs.total_score)

@router.post("/score", response_model=ScoreOut)
def finalize(session_id: int, session_db: Session = Depends(get_session),
             user=Depends(get_current_user)):
    gs = session_db.get(GameSession, session_id)
    if not gs or gs.user_id != user.id:
        raise HTTPException(status_code=404, detail="session not found")
    gs.finished_at = datetime.utcnow()
    session_db.add(gs)
    session_db.commit()

    answers = session_db.exec(select(Answer).where(Answer.session_id == gs.id)).all()
    return ScoreOut(
        session_id=gs.id,
        finished_at=gs.finished_at,
        total_score=gs.total_score,
        answers=[{
            "question_id": a.question_id,
            "option_id": a.option_id,
            "correct": a.is_correct,
            "elapsed_ms": a.elapsed_ms,
            "score_awarded": a.score_awarded,
        } for a in answers],
    )