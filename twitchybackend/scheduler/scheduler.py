from datetime import UTC, datetime, timedelta
from os import environ

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from .gamecollectionbuilder import GameCollectionBuilderScheduledTask


def start_scheduler():
    scheduler = BackgroundScheduler(
        {
            "apscheduler.executors.default": {
                "class": "apscheduler.executors.pool:ThreadPoolExecutor",
                "max_workers": "20",
            },
            "apscheduler.executors.processpool": {
                "type": "processpool",
                "max_workers": "5",
            },
            "apscheduler.job_defaults.coalesce": "false",
            "apscheduler.job_defaults.max_instances": "3",
            "apscheduler.timezone": "UTC",
        }
    )

    now = datetime.now(UTC) + timedelta(seconds=5)
    GameCollectionBuilderScheduledTask(
        scheduler, IntervalTrigger(hours=2), now
    ).schedule(now)

    if not environ.get("PYTESTING"):
        scheduler.start()
    return scheduler
