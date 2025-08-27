from typing import Any

from pydantic import BaseModel
from starlette import status


class Response(BaseModel):
    """Response"""

    code: int = status.HTTP_200_OK
    message: str = "Success."
    data: Any = None
