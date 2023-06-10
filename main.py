from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.exceptions import StarletteHTTPException
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

load_dotenv()

from env import ENV_VARS
import api, security
from db.models import QuestionCategory

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="API",
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
)


@app.get("/")
async def read_root(request: Request):
    categories = [c.value for c in QuestionCategory]
    hide_add_question = not security.AUTH_COOKIE_NAME in request.cookies
    hide_login = security.AUTH_COOKIE_NAME in request.cookies
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "categories": categories,
            "hide_add_question": hide_add_question,
            "hide_login": hide_login,
        },
    )


app.include_router(api.router, prefix="/api")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 404:
        return RedirectResponse("/")
    return


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=ENV_VARS.PORT, host="0.0.0.0")
