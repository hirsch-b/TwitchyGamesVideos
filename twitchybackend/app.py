from fastapi import FastAPI

from .api import monitoring_router, twitch_router

app = FastAPI()

app.include_router(monitoring_router)
app.include_router(twitch_router)
