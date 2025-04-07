from fastapi import FastAPI

from .api import monitoring_router

app = FastAPI()

app.include_router(monitoring_router)
