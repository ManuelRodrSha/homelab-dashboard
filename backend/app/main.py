from fastapi import FastAPI 
from app.api.health import router as health_router
from app.api.system import router as system_router


app = FastAPI(title="Homelab Monitor")

app.include_router(health_router)
app.include_router(system_router)

@app.get("/")
def root():
    return {"message": "Homelab Monitor API"}