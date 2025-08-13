import asyncio
import time
import random

async def save_to_db(sensor_ID, value):
    await asyncio.sleep(1)
    print(f"{time.ctime()} Saved {sensor_ID} = {value}")

async def main() :
    tasks = []
    for sensor_ID in range(5) :
        value = random.randint(50, 100)
        print(f"{time.ctime()} Sensor {sensor_ID} got value : {value}")
        task = asyncio.create_task(save_to_db(sensor_ID, value))
        tasks.append(task)

    await asyncio.gather(*tasks) 

asyncio.run(main())