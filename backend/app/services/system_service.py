from datetime import datetime, timezone

import psutil

from app.models.system import SystemStatus

class SystemService:
    def get_status(self) -> SystemStatus:
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory_percent = psutil.virtual_memory().percent 
        disk_percent = psutil.disk_usage("/").percent 

        boot_time = datetime.fromtimestamp(psutil.boot_time(), tz= timezone.utc)
        now = datetime.now(timezone.utc)
        uptime_seconds = (now - boot_time).total_seconds()

        return SystemStatus(
            cpu_percent= cpu_percent,
            memory_percent = memory_percent,
            disk_percent = disk_percent,
            uptime_seconds = uptime_seconds,
        )