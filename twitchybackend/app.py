from fastapi import FastAPI

from .api import monitoring_router, twitch_router
from .db import init_mongodb

app = FastAPI()

app.include_router(monitoring_router)
app.include_router(twitch_router)

init_mongodb()
