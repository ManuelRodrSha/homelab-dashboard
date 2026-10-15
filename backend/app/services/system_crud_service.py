from sqlalchemy.orm import Session
from app.models.system import System
from app.schemas.system import SystemCreate

def create_system(db: Session, system_in: SystemCreate) -> System:
    system = System(
        name=system_in.name,
        hostname=system_in.hostname,
        ip_address=system_in.ip_address,
    )
    db.add(system)
    db.commit()
    db.refresh(system)
    return system

def get_systems(db: Session) -> list[System]:
    return db.query(System).order_by(System.id.asc()).all()

def get_system_by_id(db: Session, system_id: int) -> System | None:
    return db.query(System).filter(System.id == system_id).first()