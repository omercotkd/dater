from fastapi import FastAPI
from env import ENV_VARS

app = FastAPI(
    title="API",
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=ENV_VARS.PORT, host="0.0.0.0")
