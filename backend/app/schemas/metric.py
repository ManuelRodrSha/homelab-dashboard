from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MetricSampleCreate(BaseModel):
    system_id: int
    metric_name: str   # cpu, memory, disk
    value: float
    unit: str = "%"

class MetricSampleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    system_id: int
    metric_name: str
    value: float
    unit: str
    timestamp: datetime