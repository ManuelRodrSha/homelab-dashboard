from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class MetricSample(Base):
    __tablename__ = "metric_samples"

    id = Column(Integer, primary_key=True, index=True)
    system_id = Column(Integer, ForeignKey("systems.id"), nullable=False, index=True)
    metric_name = Column(String, nullable=False, index=True)  # cpu, memory, disk...
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False, default="%")
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)