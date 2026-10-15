from datetime import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.metric import MetricSampleCreate, MetricSampleRead
from app.services.metric_service import (
    create_metric_sample,
    get_metrics_by_system,
)

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.post("", response_model=MetricSampleRead, status_code=status.HTTP_201_CREATED)
def create_metric_endpoint(
    metric_in: MetricSampleCreate,
    db: Session = Depends(get_db),
):
    return create_metric_sample(db, metric_in)


@router.get("/systems/{system_id}", response_model=list[MetricSampleRead])
def get_metrics_for_system(
    system_id: int,
    metric_name: str | None = None,
    start: datetime | None = None,
    end: datetime | None = None,
    limit: int | None = None,
    db: Session = Depends(get_db),
):
    return get_metrics_by_system(
        db=db,
        system_id=system_id,
        metric_name=metric_name,
        start=start,
        end=end,
        limit=limit,
    )