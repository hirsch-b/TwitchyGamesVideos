from datetime import UTC, datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from .gamecollectionbuilder import GameCollectionBuilderScheduledTask

scheduler = None


def get_scheduler():
    global scheduler
    if scheduler is None:
        # scheduler = AsyncIOScheduler(
        scheduler = BackgroundScheduler(
            {
                # "apscheduler.jobstores.mongo": {"type": "mongodb"},
                # "apscheduler.jobstores.default": {
                #     "type": "sqlalchemy",
                #     "url": "sqlite:///jobs.sqlite",
                # },
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

        # scheduler.add_job(
        #     lambda: asyncio.run(build_games_collection()),
        #     IntervalTrigger(hours=2),
        #     next_run_time=datetime.now(UTC),
        #     id="build_games_collection",
        # )

        # scheduler.start()
        now = datetime.now(UTC) + timedelta(seconds=5)
        GameCollectionBuilderScheduledTask(
            scheduler, IntervalTrigger(hours=2), now
        ).schedule(now)

    return scheduler
