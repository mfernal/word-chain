from fastapi import FastAPI
from app.backend.api.api import api_router
from app.backend.core.settings import API

app = FastAPI(
    title='FastAPI backend',
    description='Word Chain',
)

app.include_router(
    api_router,
    prefix=API.BASE
    )
