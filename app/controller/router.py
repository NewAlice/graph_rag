from fastapi import APIRouter

from app.config import AppSettings
from app.controller.health import HealthController

settings = AppSettings()
PREFIX = settings.SVC_PREFIX

api_router = APIRouter()

api_router.include_router(
    HealthController.router,
    prefix=PREFIX + "/v1/health",
    tags=["Health"],
    dependencies=None,
)
