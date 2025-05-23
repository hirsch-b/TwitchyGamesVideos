import logging
from os import environ

from mongoengine import connect
from redis import Redis

from twitchybackend.models.game import Game
from twitchybackend.clients.twitch import get_client
from twitchAPI.helper import limit

logger = logging.getLogger(__name__)
redis: Redis = None


def init_mongodb():
    host = environ.get("MONGODB_HOST", "localhost")
    port = environ.get("MONGODB_PORT", "27017")
    db = environ.get("MONGODB_DB", "twitchybackend")
    mongodb_connection = connect(
        host=f"mongodb://{host}:{port}/{db}",
        uuidRepresentation="standard",
        tz_aware=True,
    )
    return mongodb_connection


def init_redis():
    global redis
    if redis is None:
        host = environ.get("REDIS_HOST", "localhost")
        port = environ.get("REDIS_PORT", "6379")
        db = environ.get("REDIS_DB", "0")
        redis = Redis(host, port, db)
    return redis
