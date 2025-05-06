import logging

from fastapi import FastAPI

from .api import monitoring_router, twitch_router
from .db import init_mongodb, init_redis
from .scheduler import start_scheduler

uvicorn_logger = logging.getLogger("uvicorn")
root_logger = logging.getLogger()
root_logger.setLevel(uvicorn_logger.level)
for uvicorn_handler in uvicorn_logger.handlers:
    root_logger.addHandler(uvicorn_handler)

logger = logging.getLogger(__name__)

mongodb = init_mongodb()
redis = init_redis()
scheduler = start_scheduler()

app = FastAPI(title="TwitchyApp")

app.include_router(monitoring_router)
app.include_router(twitch_router)
