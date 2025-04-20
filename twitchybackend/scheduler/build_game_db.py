import logging

from twitchAPI.helper import limit
from twitchybackend.db import init_redis
from twitchybackend.db import get_client
from twitchybackend.models.game import Game

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def build_games_collection():
    logger.info("%d games exist in the database", Game.objects().count())
    lock = init_redis().lock(__name__)
    if lock.acquire(blocking=False):
        client = await get_client()
        for letter in "abcdefghijklmnopqrstuvwxyz":
            count = Game.objects(name__startswith=letter).count()
            logger.info("%d games for the letter %s in the DB", count, letter)
            if count == 0:
                async for game in limit(
                    client.search_categories(letter, first=100), 500
                ):
                    Game.objects(twitch_id=game.id).update(
                        set__name=game.name,
                        set__box_art_url=game.box_art_url,
                        upsert=True,
                    )
    else:
        logger.debug("Database loading is already running")
