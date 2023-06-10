from argon2 import PasswordHasher
import jwt
from env import ENV_VARS
from db.models import Writers
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder

ph = PasswordHasher()

AUTH_COOKIE_NAME = "auth_token"


class TokenPayload(BaseModel):
    username: Writers = Field(...)


def verify_password(password, hash):
    try:
        ph.verify(hash, password)
        return True
    except:
        return False


def hash_password(password):
    return ph.hash(password)


def create_access_token(username: Writers):
    return jwt.encode(
        payload=jsonable_encoder(TokenPayload(username=username).dict()),
        key=ENV_VARS.SECRET_KEY,
        algorithm="HS256",
    )


def decode_access_token(token: str):
    try:
        data = jwt.decode(token, ENV_VARS.SECRET_KEY, algorithms=["HS256"])
        return TokenPayload(**data)
    except:
        return None
