from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager, suppress
import asyncio

from app.api.health import router as health_router
from app.api.system import router as system_router
from app.api.docker import router as docker_router
from app.api.metrics import router as metrics_router
from app.api.systems import router as systems_router

from app.db.base import Base
from app.db.session import engine
from app.models import System, MetricSample, Event
from app.services.snapshot_runner import snapshot_loop


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[main] lifespan arrancado", flush=True)
    task = asyncio.create_task(snapshot_loop(interval_seconds=30))
    try:
        yield
    finally:
        print("[main] cancelando snapshot loop", flush=True)
        task.cancel()
        with suppress(asyncio.CancelledError):
            await task


app = FastAPI(title="Homelab Monitor", lifespan=lifespan)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(system_router)
app.include_router(systems_router)
app.include_router(docker_router)
app.include_router(metrics_router)


@app.get("/")
def root():
    return {"message": "Homelab Monitor API"}