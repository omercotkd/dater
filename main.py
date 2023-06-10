from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from env import ENV_VARS
import api

app = FastAPI(
    title="API",
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
)

app.include_router(api.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=ENV_VARS.PORT, host="0.0.0.0")
