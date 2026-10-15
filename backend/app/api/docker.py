from fastapi import APIRouter, HTTPException
from docker.errors import DockerException

from app.services.docker_service import DockerService
from app.schemas.docker import DockerContainer

router = APIRouter(prefix="/docker", tags=["docker"])

@router.get("/containers", response_model=list[DockerContainer])
def get_containers():
    service = DockerService()
    try:
        return service.get_running_containers()
    except DockerException:
        raise HTTPException(
            status_code = 503,
            detail="No se pudo conectar con Docker",
        )
