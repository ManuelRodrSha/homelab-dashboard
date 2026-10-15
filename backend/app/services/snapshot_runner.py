import asyncio
from app.db.session import SessionLocal
from app.services.system_crud_service import get_systems
from app.services.system_snapshot_service import create_system_snapshot

async def snapshot_loop(interval_seconds: int = 10):
    print(f"[snapshot_loop] arrancado cada {interval_seconds}s", flush=True)

    while True:
        db = SessionLocal()
        try:
            systems = get_systems(db)
            print(f"[snapshot_loop] systems encontrados: {len(systems)}", flush=True)

            for system in systems:
                print(f"[snapshot_loop] creando snapshot system_id={system.id}", flush=True)
                create_system_snapshot(db, system.id)
                print(f"[snapshot_loop] snapshot OK system_id={system.id}", flush=True)

        except Exception as e:
            print(f"[snapshot_loop] ERROR: {e}", flush=True)
        finally:
            db.close()

        await asyncio.sleep(interval_seconds)