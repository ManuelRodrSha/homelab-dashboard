from datetime import datetime, timedelta, timezone 
import app.services.system_service as system_service_module
from app.services.system_service import SystemService

def test_gets_status(monkeypatch):
    fixed_boot_time = datetime.now(timezone.utc) - timedelta(hours = 2)

    monkeypatch.setattr(system_service_module.psutil, "cpu_percent", lambda interval=0.1:12.5)

    class MockMemory:
        percent = 45.0

    class MockDisk:
        percent = 67.0

    monkeypatch.setattr(system_service_module.psutil, "virtual_memory", lambda: MockMemory())
    monkeypatch.setattr(system_service_module.psutil, "disk_usage", lambda path: MockDisk())
    monkeypatch.setattr(system_service_module.psutil, "boot_time", lambda: fixed_boot_time.timestamp())

    service = SystemService()
    result = service.get_status()

    assert result.cpu_percent == 12.5
    assert result.memory_percent == 45.0
    assert result.disk_percent == 67.0
    assert 7199 <= result.uptime_seconds <= 7201