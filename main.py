from fastapi import FastAPI, Request, Path
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

from env import ENV_VARS
import api

app = FastAPI(
    title="API",
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
)

app.include_router(api.router, prefix="/api")

app.mount("/assets", StaticFiles(directory="front/dist"), name="static")

@app.get("/")
def index():
    return RedirectResponse("/assets/index.html")

@app.exception_handler(404)
def not_found(request: Request, exc: HTTPException):
    
    return RedirectResponse(f"/assets{request.url.path}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=ENV_VARS.PORT, host="0.0.0.0")
