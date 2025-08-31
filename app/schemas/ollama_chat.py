from pydantic import BaseModel, Field



class OllamaChatContent(BaseModel):
    content: str = Field(...)