import asyncio
import random
import time

async def save_to_db(sensor_ID, value) :
    await asyncio.sleep(1)
    if value > 80 :
        raise ValueError(f"Sensor {sensor_ID} value {value} is too high!")
    print(f"{time.ctime()} Saved {sensor_ID} = {value}")

async def handle_sensor(sensor_ID) :
    value = random.randint(50, 100)
    print(f"{time.ctime()} Sensor {sensor_ID} got value : {value}")    
    asyncio.create_task(save_to_db(sensor_ID, value)) # no await

async def main():
    for i in range(5):
        await handle_sensor(i)
    await asyncio.sleep(0.5)

asyncio.run(main()) 