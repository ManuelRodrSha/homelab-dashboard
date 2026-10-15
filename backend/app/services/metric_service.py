from datetime import datetime
from sqlalchemy.orm import Session

from app.models.metric_sample import MetricSample
from app.schemas.metric import MetricSampleCreate
from app.schemas.system import SystemStatus


def create_metric_sample(db: Session, metric_in: MetricSampleCreate) -> MetricSample:
    metric = MetricSample(
        system_id=metric_in.system_id,
        metric_name=metric_in.metric_name,
        value=metric_in.value,
        unit=metric_in.unit,
    )
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric


def save_status_metrics(db: Session, system_id: int, status: SystemStatus):
    samples = [
        MetricSample(system_id=system_id, metric_name="cpu", value=status.cpu_percent, unit="%"),
        MetricSample(system_id=system_id, metric_name="memory", value=status.memory_percent, unit="%"),
        MetricSample(system_id=system_id, metric_name="disk", value=status.disk_percent, unit="%"),
        MetricSample(system_id=system_id, metric_name="uptime", value=status.uptime_seconds, unit="s"),
    ]

    db.add_all(samples)
    db.commit()

    for sample in samples:
        db.refresh(sample)

    return samples


def get_metrics_by_system(
    db: Session,
    system_id: int,
    metric_name: str | None = None,
    start: datetime | None = None,
    end: datetime | None = None,
    limit: int | None = None,
):
    query = db.query(MetricSample).filter(MetricSample.system_id == system_id)

    if metric_name:
        query = query.filter(MetricSample.metric_name == metric_name)

    if start:
        query = query.filter(MetricSample.timestamp >= start)

    if end:
        query = query.filter(MetricSample.timestamp <= end)

    query = query.order_by(MetricSample.timestamp.asc())

    if limit:
        query = query.limit(limit)

    return query.all()