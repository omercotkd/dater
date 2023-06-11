from fastapi import APIRouter, Response, Depends, Request
from pydantic import BaseModel, Field
from db.models import Question
import db
from ..middlewares import login_required
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

router = APIRouter(
    dependencies=[Depends(login_required)],
)


class QuestionPayload(BaseModel):
    text: str = Field(...)
    for_whom: str = Field(..., alias="forWhom")


@router.post("/")
def create_question(
    request: Request,
    payload: QuestionPayload,
):

    question = Question(
        text=payload.text,
        writer=request.state.writer,
        for_whom=payload.for_whom,
    )
    try:
        db.QUESTIONS.insert_one(question.dict())
    except Exception as e:
        print(e)
        return Response(status_code=500)

    return Response(status_code=201)

@router.get("/my")
def get_my_questions(request: Request):
    try:
        questions = db.QUESTIONS.find({"writer": request.state.writer})
    except Exception as e:
        print(e)
        return Response(status_code=500)
    return jsonable_encoder({
        "success": True,
        "data": list(questions),
    }, custom_encoder={ObjectId: str})

