from os import environ

from mongoengine import connect


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
