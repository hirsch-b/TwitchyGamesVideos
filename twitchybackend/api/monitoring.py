from datetime import UTC, datetime

from fastapi import APIRouter

router = APIRouter(prefix="/monitoring")


@router.get("/heartbeat")
def heartbeat():
    return {"now": datetime.now(UTC)}
