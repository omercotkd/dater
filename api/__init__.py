from fastapi import APIRouter
from .routes import login, questions

router = APIRouter()

router.include_router(login.router, tags=["login"], prefix="/login")
router.include_router(questions.router, tags=["questions"], prefix="/questions")
