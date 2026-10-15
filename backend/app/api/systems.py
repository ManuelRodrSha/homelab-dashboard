from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.system import SystemCreate, SystemRead, SystemStatus
from app.services.system_crud_service import (
    create_system,
    get_systems,
    get_system_by_id,
)

router = APIRouter(prefix="/systems", tags=["systems"])

@router.post("", response_model=SystemRead, status_code=status.HTTP_201_CREATED)
def create_system_endpoint(
    system_in: SystemCreate,
    db: Session = Depends(get_db),
):
    return create_system(db, system_in)

@router.get("", response_model=list[SystemRead])
def list_systems_endpoint(db: Session = Depends(get_db)):
    return get_systems(db)

@router.get("/{system_id}", response_model=SystemRead)
def get_system_endpoint(system_id: int, db: Session = Depends(get_db)):
    system = get_system_by_id(db, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")
    return system

@router.post("/{system_id}/snapshot", response_model=SystemStatus)
def snapshot_system_endpoint(
    system_id: int,
    db: Session = Depends(get_db),
):
    system = get_system_by_id(db, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")

    return create_system_snapshot(db, system_id)