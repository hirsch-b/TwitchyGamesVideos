from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from .api import monitoring_router, twitch_router
from .db import init_mongodb, build_games_collection

logger = logging.getLogger(__name__)

init_mongodb()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await build_games_collection()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(monitoring_router)
app.include_router(twitch_router)
