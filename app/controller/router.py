from fastapi import APIRouter

from app.config import AppSettings
from app.controller.health import HealthController
from app.controller.ollama_chat import OllamaChatController

settings = AppSettings()
PREFIX = settings.SVC_PREFIX

api_router = APIRouter()

api_router.include_router(
    HealthController.router,
    prefix=PREFIX + "/v1/health",
    tags=["Health"],
    dependencies=None,
)

api_router.include_router(
    OllamaChatController.router,
    prefix=PREFIX + "/v1/chat",
    tags=["chat"],
    dependencies=None,
)