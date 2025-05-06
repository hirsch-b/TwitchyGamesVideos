import logging

from twitchAPI.helper import limit
from twitchybackend.db import redis
from twitchybackend.db import init_redis
from twitchybackend.db import get_client
from twitchybackend.models.game import Game

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def pre_build_games_collection():
    redis.delete(__name__)


async def build_games_collection():
    logger.info("%d games exist in the database", Game.objects().count())
    lock = redis.lock(__name__, timeout=3600 * 2)
    if lock.acquire(blocking=False):
        client = await get_client()
        for letter in "abcdefghijklmnopqrstuvwxyz":
            count = Game.objects(name__istartswith=letter).count()
            logger.debug(
                "%d games for the letter %s in the DB", count, letter.upper()
            )
            if limit is None or count < limit:
                async for game in limit(
                    client.search_categories(letter, first=100), 500
                ):
                    Game.objects(twitch_id=game.id).update(
                        set__name=game.name,
                        set__box_art_url=game.box_art_url,
                        upsert=True,
                    )
        lock.release()
    else:
        logger.debug("Database loading is already running")
