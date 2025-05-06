import logging

from twitchAPI.helper import limit

from twitchybackend.db import get_client
from twitchybackend.models.game import Game
from twitchybackend.scheduler.asyncscheduledtask import AsyncScheduledTask

logger = logging.getLogger(__name__)


class GameCollectionBuilderScheduledTask(AsyncScheduledTask):
    name = "GameCollectionBuilderScheduledTask"

    async def _job(self):
        logger.info("%d games exist in the database", Game.objects().count())
        lock = self.redis.lock(__name__, timeout=3600 * 2)
        if lock.acquire(blocking=False):
            client = await get_client()
            for letter in "abcdefghijklmnopqrstuvwxyz":
                count = Game.objects(name__istartswith=letter).count()
                logger.info(
                    "%d games for the letter %s in the DB",
                    count,
                    letter.upper(),
                )
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
