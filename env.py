from pydantic import BaseSettings


class EnvVars(BaseSettings):
    DB_CONNECTION_STRING: str
    DB_NAME: str
    PORT: int


ENV_VARS = EnvVars()
