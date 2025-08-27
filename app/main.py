import logging
import os.path
from contextlib import asynccontextmanager
from http import HTTPStatus

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from pydantic import ValidationError
from starlette import status
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from app.config import AppSettings
from app.controller.router import api_router
from app.schemas.response import Response

settings = AppSettings()
PREFIX = settings.SVC_PREFIX

logger = logging.getLogger(__name__)


async def http_exception_handler(request: Request, exc: HTTPException):
    data = Response(code=exc.status_code, data=None, message=str(exc.detail))
    return JSONResponse(data.model_dump(), status_code=exc.status_code)


def base_exception_handler(request: Request, exc: HTTPException):
    return exc.to_json_response()


async def validation_exception_handler(request: Request, exc: ValidationError):
    response = Response(
        code=status.HTTP_400_BAD_REQUEST, data=None, message=str(exc.errors())
    )
    return JSONResponse(response.model_dump(), status_code=HTTPStatus.OK)


async def param_exception_handler(request: Request, err: Exception):
    data = Response(code=status.HTTP_400_BAD_REQUEST, data=None, message=str(err))
    return JSONResponse(data.model_dump(), status_code=HTTPStatus.OK)


async def exception_handler(request: Request, exc: Exception):
    err = "Internal Exception"
    if len(exc.args) > 0:
        err = str(exc.args[0])
    elif "detail" in exc.__dict__:
        err = exc.__dict__.get("detail")

    code = status.HTTP_400_BAD_REQUEST
    if "status_code" in exc.__dict__:
        code = exc.__dict__.get("status_code")

    data = Response(code=code, data=None, message=err)
    return JSONResponse(data.model_dump(), status_code=HTTPStatus.OK)


def init_routes(_app):
    _app.include_router(api_router)
    # _app = init_exception_handler(_app)


def init_extensions(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
        allow_headers=settings.CORS_HEADERS,
    )


def init_exception_handlers(app):
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    # app.add_exception_handler(BaseDPException, base_dp_exception_handler)
    app.add_exception_handler(Exception, exception_handler)
    app.add_exception_handler(HTTPException, base_exception_handler)


def configure_static(app):
    bese_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    app.mount(
        PREFIX + "/static",
        StaticFiles(directory=os.path.join(bese_path, "static")),
        name="static",
    )


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


def create_app() -> FastAPI:
    app_config = {
        "debug": settings.DEBUG,
        "docs_url": None,
        "redoc_url": None,
        "openapi_url": f"{settings.SVC_PREFIX}/openapi.json",
        "title": f"{settings.APP_NAME} service",
        "version": settings.DEVOPS_VERSION,
    }
    app_config["lifespan"] = lifespan
    app = FastAPI(**app_config)

    init_routes(app)
    init_extensions(app)
    init_exception_handlers(app)
    configure_static(app)

    return app


app = create_app()


@app.get(PREFIX + "/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url="static/swagger-ui/swagger-ui.css",
        swagger_favicon_url="static/swagger-ui/favicon-32x32.png",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get(PREFIX + "/redoc", include_in_schema=False)
async def custom_redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@2/bundles/redoc.standalone.js",
        redoc_favicon_url="static/redoc/favicon.png",
    )


@app.get("/", include_in_schema=False)
def read_root():
    print(PREFIX)
    return RedirectResponse(PREFIX + "/docs")


@app.get(PREFIX, include_in_schema=False)
def read_root_prefix():
    return RedirectResponse(PREFIX + "/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
