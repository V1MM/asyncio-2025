# file: rocketapp.py

from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):
    """
    TODO:
    - จำลองเวลาจรวดด้วย random delay 1-2 วินาที
    - print log ว่า rocket launched และ reached destination
    """
    delay = random.uniform(1,2)
    await asyncio.sleep(delay)
    print(f"Rocket {student_id} launched! ETA : {delay} seconds") 
    print(f"Rocket {student_id} reached destination after {delay} seconds")


@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    """
    TODO:
    - ตรวจสอบ student_id ต้องเป็น 10 หลัก
    - สร้าง background task ยิง rocket
    - รอ random delay 1-2 วินาที ก่อนส่ง response
    - return dict {"message": ..., "time_to_target": ...}
    """
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="Invalid student ID. Must be 10 digits.")
    
    delay = random.uniform(1,2)
    asyncio.create_task(launch_rocket(student_id))
    await asyncio.sleep(delay)
    
    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": delay
    }
