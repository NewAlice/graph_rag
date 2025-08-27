from pydantic_settings import BaseSettings
from typing import List

class AppSettings(BaseSettings):
    FAKE_SESSION: str = "eyJsb2dpbl9pZCI6ICJ6bGluZy53YW5nIiwgInVzZXIiOiB7ImlkIjogMTM1MjIsICJjcmVhdGVfdXNlciI6ICJ6bGluZy53YW5nIiwgImNyZWF0ZV90aW1lIjogIjIwMjQtMTAtMTVUMDM6NDc6MDYiLCAidXBkYXRlX3VzZXIiOiBudWxsLCAidXBkYXRlX3RpbWUiOiAiMjAyNS0wOC0xOFQwNjo0MDoxMSIsICJkZXNjcmlwdGlvbiI6IG51bGwsICJ0YWdzIjogbnVsbCwgImxvZ2luX2lkIjogInpsaW5nLndhbmciLCAiZW1haWwiOiAiemxpbmcud2FuZ0BzYW1zdW5nLmNvbSIsICJkZXB0bmFtZV9lbiI6ICJTZXJ2aWNlIERldmVsb3BtZW50IFBhcnQgL1NTQ1IiLCAidXNlcm5hbWVfZW4iOiAiWmhlbmxpbmcgV2FuZyIsICJzdGF0dXMiOiAidXNlcl9ub3JtYWwiLCAiaXNfZGVsZXRlZCI6IGZhbHNlLCAiZW5hYmxlIjogdHJ1ZSwgImVuYWJsZV90aW1lIjogIjIwMjQtMTAtMTVUMDM6NDc6MDYiLCAiZGlzYWJsZV90aW1lIjogbnVsbCwgImxvZ2luX3RpbWUiOiAiMjAyNS0wOC0yNlQwMTo0NDozMiIsICJqb2JfZGVzY3JpcHRpb24iOiAiIiwgImF2YXRhciI6IG51bGwsICJ0aW1lem9uZSI6IG51bGwsICJzc29fdXNlciI6IHt9LCAicHJldmlvdXNfc3NvX3VzZXIiOiB7fX0sICJzZXNzaW9uX2lkIjogInNlc3Npb246emxpbmcud2FuZzo1YWNjNjIxZGQ2NWI0ODFiYTJhMDQ0OWM4YmMyMmU5MCJ9.aK0RiA.kGO4ZbEfOz38FT1m-IcDx2cBF7I"
    ENVIRONMENT: str = "prod"
    DEBUG: bool = True

    VERSION: str = "test"
    APP_NAME: str = "graph-rag"
    APP_ID: str = "1"

    SVC_PREFIX: str = "/api"

    CORS_ORIGINS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]

    # Custom settings
    disable_docs: bool = False
