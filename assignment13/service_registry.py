# service_registry.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Service Registry")

# เก็บข้อมูล service ของนักเรียนทั้งหมด
registry: Dict[str, Dict] = {}

class ServiceInfo(BaseModel):
    name: str
    url: str
    city: str

# -------------------------
# 1. ดูรายชื่อ service ทั้งหมด
# -------------------------
@app.get("/services")
def get_services():
    return {"services": list(registry.values())}

# -------------------------
# 2. สมัคร service
# -------------------------
@app.post("/register")
def register_service(service: ServiceInfo):
    if service.name in registry:
        raise HTTPException(status_code=400, detail="Service already registered")
    registry[service.name] = service.model_dump()

    return {"message": f"Service {service.name} registered successfully."}

# -------------------------
# 3. อัปเดต service
# -------------------------
@app.put("/update")
def update_service(service: ServiceInfo):
    if service.name not in registry:
        raise HTTPException(status_code=404, detail="Service not found")
    registry[service.name] = service.model_dump()

    return {"message": f"Service {service.name} updated successfully."}

# -------------------------
# 4. ยกเลิก service
# -------------------------
@app.delete("/unregister/{name}")
def unregister_service(name: str):
    if name not in registry:
        raise HTTPException(status_code=404, detail="Service not found")
    del registry[name]
    return {"message": f"Service {name} unregistered successfully."}
