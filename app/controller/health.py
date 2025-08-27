from fastapi import APIRouter

from app.schemas.response import Response


class HealthController:
    router = APIRouter()

    @staticmethod
    @router.get("")
    def health() -> Response:
        return Response()
