from pydantic import BaseSettings


class EnvVars(BaseSettings):
    DB_CONNECTION_STRING: str
    DB_NAME: str
    PORT: int
    SECRET_KEY: str


ENV_VARS = EnvVars()
