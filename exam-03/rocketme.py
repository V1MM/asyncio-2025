#✅ Complete
import time
import asyncio
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict


student_id = "6610301012"

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์
    """
    TODO:
    - ส่ง GET request ไปยัง rocketapp ที่ path /fire/{student_id}
    - อ่านค่า time_to_target จาก response
    - return dict ที่มี:
        {
            "name": name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }
    """   
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="[ERROR] failed to fire Rocket Please stand by")
        data = response.json()
        time_to_target = data["time_to_target"]
        end_time = start_time + time_to_target
        return {
            "name" : name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }


async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")  # แสดงตอนเริ่ม main

    # TODO: สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = []
    for i in range(3) :
        name = f"Rocket-{i+1}"
        tasks.append ( asyncio.create_task(fire_rocket(name,t0)) )

    # TODO: รอให้ทุก task เสร็จและเก็บผลลัพธ์ตามลำดับ task
    results = []
    for task in tasks :
        result = await task 
        results.append(result)


    # TODO: แสดงผล start_time, time_to_target, end_time ของแต่ละ rocket ตามลำดับ task
    print("Rockets fired:")
    for r in results: 
        print(f"{r['name']} | Start Time: {r['start_time']:.2f} sec | Time to Target: {r['time_to_target']:.2f} sec | End Time: {r['end_time']:.2f} sec")

    # TODO: แสดงเวลารวมทั้งหมดตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย
    t_total = 0  # คำนวณ max end_time
    t_total = time.perf_counter() - t0
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")
    print("Mission complete.")

if __name__ == "__main__":
    asyncio.run(main())

