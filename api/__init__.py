from fastapi import APIRouter, Depends
from .routes import login, questions
from .middlewares import login_required

router = APIRouter()

router.include_router(login.router, tags=["login"], prefix="/login")
router.include_router(questions.router, tags=["questions"], prefix="/questions")

@router.get("/me", dependencies=[Depends(login_required)])
def me():
    return {
        "success": True,
        "message": "You are logged in",
    }