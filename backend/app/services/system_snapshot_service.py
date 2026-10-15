from sqlalchemy.orm import Session

from app.schemas.system import SystemStatus
from app.services.system_service import SystemService
from app.services.metric_service import save_status_metrics


def create_system_snapshot(db: Session, system_id: int) -> SystemStatus:
    service = SystemService()
    status = service.get_status()

    save_status_metrics(db, system_id, status)

    return status