import asyncio
from datetime import datetime

from twitchybackend.scheduler.scheduledtask import ScheduledTask


class AsyncScheduledTask(ScheduledTask):
    def _pre_job(self, next_run_time):
        self.redis.delete(self.name)

    async def _job(self):
        pass

    def schedule(self, next_run_time: datetime):
        self.scheduler.add_job(
            lambda: asyncio.run(self._job()),
            self.interval,
            next_run_time=next_run_time,
            id=self.name,
        )
