from fastapi import APIRouter

from app.services.system_service import SystemService

router = APIRouter(prefix = "/system", tags=['system'])

@router.get("")
def get_system_status():
    service = SystemService()
    return service.get_status()
