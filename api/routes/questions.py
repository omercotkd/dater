from fastapi import APIRouter, Response, Depends, Request
from pydantic import BaseModel, Field
from db.models import Writers, QuestionCategory, Question
import db
from ..middlewares import login_required

router = APIRouter(
    dependencies=[Depends(login_required)],
)


class QuestionPayload(BaseModel):
    text: str = Field(...)
    category: QuestionCategory = Field(...)


@router.post("/")
def create_question(
    request: Request,
    payload: QuestionPayload,
):
    print(request.headers)
    question = Question(
        text=payload.text,
        category=payload.category,
        writer=request.state.writer,
    )
    try:
        db.QUESTIONS.insert_one(question.dict())
    except Exception as e:
        print(e)
        return Response(status_code=500)

    return Response(status_code=201)
