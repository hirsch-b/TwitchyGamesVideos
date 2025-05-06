import asyncio
from datetime import datetime
from inspect import iscoroutinefunction
from typing import Optional
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


class ScheduledTask:
    def __init__(
        self,
        name: str,
        scheduler: BackgroundScheduler,
        interval: IntervalTrigger,
        next_run_time: Optional[datetime] = None,
    ):
        self.scheduler = scheduler

        self.scheduler.add_job(
            self._job, interval, next_run_time=next_run_time, id=name
        )

    def _pre_job(self):
        pass

    def _job(self):
        pass
