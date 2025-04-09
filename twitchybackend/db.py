import logging
from os import environ

from mongoengine import connect

from twitchybackend.models.game import Game
from twitchybackend.clients.twitch import get_client
from twitchAPI.helper import limit

logger = logging.getLogger(__name__)


def init_mongodb():
    host = environ.get("MONGODB_HOST", "mongo")
    host = environ.get("MONGODB_HOST", "localhost")
    port = environ.get("MONGODB_PORT", "27017")
    db = environ.get("MONGODB_PORT", "twitchybackend")
    mongodb_connection = connect(
        host=f"mongodb://{host}:{port}/{db}",
        uuidRepresentation="standard",
        tz_aware=True,
    )
    return mongodb_connection


async def build_games_collection():
    logger.info("%d games exist in the database", Game.objects().count())
    client = await get_client()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        count = Game.objects(name__startswith=letter).count()
        logger.info("%d games for the letter %s in the DB", count, letter)
        if count == 0:
            async for game in limit(client.search_categories(letter, first=100), 500):
                Game.objects(twitch_id=game.id).update(
                    set__name=game.name,
                    set__box_art_url=game.box_art_url,
                    upsert=True
                )
