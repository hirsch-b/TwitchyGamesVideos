from datetime import UTC, datetime

from fastapi import APIRouter, Response
from pymongo.errors import ConnectionFailure

from twitchybackend.db import mongodb, redis

router = APIRouter(prefix="/monitoring")


@router.get("/heartbeat")
def heartbeat():
    return {"now": datetime.now(UTC)}


@router.get("/status")
def status(response: Response):
    print(mongodb)
    redis_status = None
    mongodb_status = None

    try:
        redis_status = redis.info().get("server_time_usec")
    except:
        pass

    try:
        mongodb_status = mongodb.admin.command("ping")
    except ConnectionFailure:
        pass

    response.status_code = (
        200 if redis_status is not None and mongodb_status is not None else 500
    )
    return {"redis": redis_status, "mongodb": mongodb_status is not None}
