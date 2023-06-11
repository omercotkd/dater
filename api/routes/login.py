from fastapi import APIRouter, Response, Depends
from pydantic import BaseModel, Field
from db.models import Writers
import security
from ..middlewares import guest_required

router = APIRouter(
    dependencies=[Depends(guest_required)],
)


class LoginPayload(BaseModel):
    username: Writers = Field(...)
    password: str = Field(...)


@router.post("/")
def login(
    payload: LoginPayload,
):
    if not security.verify_password(payload.password, payload.username.get_password()):
        return Response(status_code=401)

    res = Response()

    res.set_cookie(
        key=security.AUTH_COOKIE_NAME,
        value=security.create_access_token(payload.username),
        httponly=True,
        max_age=60 * 60 * 24 * 7,
    )

    res.body = {
        "success": True,
        "message": "Login successful",
    }
    
    return res
