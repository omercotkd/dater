from fastapi import Depends, Request, HTTPException
from fastapi.security import APIKeyCookie
import security


login_required_scheme = APIKeyCookie(
    name=security.AUTH_COOKIE_NAME,
    scheme_name="User Access Token",
    description="Token to validate that the user is logged in will be added to the cookies after login",
)


def login_required(request: Request, token: str = Depends(login_required_scheme)):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token_data = security.decode_access_token(token)

    if not token_data:
        raise HTTPException(status_code=401, detail="Not authenticated")

    request.state.writer = token_data.username


def guest_required(request: Request):
    token = request.cookies.get(security.AUTH_COOKIE_NAME)

    if token:
        token_data = security.decode_access_token(token)
        if token_data:
            raise HTTPException(status_code=401, detail="Already authenticated")
        else:
            # TODO - remove the cookie
            pass
