from datetime import datetime
from typing import Optional

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from twitchybackend.db import init_redis


class ScheduledTask:
    name = None

    def __init__(
        self,
        scheduler: BackgroundScheduler,
        interval: IntervalTrigger,
        next_run_time: Optional[datetime] = None,
    ):
        self.redis = init_redis()
        self.scheduler = scheduler
        self.interval = interval

        self._pre_job(next_run_time)

    def schedule(self, next_run_time):
        self.scheduler.add_job(
            self._job, self.interval, next_run_time=next_run_time, id=self.name
        )

    def _pre_job(self):
        self.redis.delete(self.name)

    def _job(self):
        pass
