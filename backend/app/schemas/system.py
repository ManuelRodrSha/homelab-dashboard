from pydantic import BaseModel, ConfigDict

class SystemStatus(BaseModel):
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    uptime_seconds: float
    
class SystemCreate(BaseModel):
    name: str 
    hostname: str | None = None 
    ip_address: str | None = None 

class SystemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int 
    name: str 
    hostname: str | None = None 
    id_address: str | None = None 