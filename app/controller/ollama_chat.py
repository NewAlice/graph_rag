from fastapi import APIRouter, Query
from ollama import chat
from ollama import ChatResponse

from app.schemas.ollama_chat import OllamaChatContent
from app.schemas.response import Response

QWEN_MODEL = "qwen3:8b"


class OllamaChatController:
    router = APIRouter()

    @staticmethod
    @router.get("")
    def chat(question: str = Query(description="chat question")) -> Response:
        response: ChatResponse = chat(
            model=QWEN_MODEL,
            messages=[{"role": "user", "content": question}],
        )
        if getattr(response, "message"):
            data = response.message.content
        else:
            data = response["message"]["content"]
        return Response(data=OllamaChatContent(content=data))
