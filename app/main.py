from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import users, auth

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(auth.router)
app.include_router(users.router)
