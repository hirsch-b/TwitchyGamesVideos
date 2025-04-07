from datetime import datetime, UTC
from fastapi import APIRouter

router = APIRouter(prefix="/monitoring")


@router.get("/heartbeat")
def heartbeat():
    return {"now": datetime.now(UTC)}
