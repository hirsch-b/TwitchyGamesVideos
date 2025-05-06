from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from .api import monitoring_router, twitch_router
from .db import init_mongodb, init_redis
from .scheduler import get_scheduler

uvicorn_logger = logging.getLogger("uvicorn")
root_logger = logging.getLogger()
root_logger.handlers = uvicorn_logger.handlers

logger = logging.getLogger(__name__)

mongodb = init_mongodb()
redis = init_redis()
scheduler = get_scheduler()

scheduler.start()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await build_games_collection()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(monitoring_router)
app.include_router(twitch_router)
