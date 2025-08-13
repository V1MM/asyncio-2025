import  asyncio, time , random

async def get_temperature() :
    await asyncio.sleep(random.uniform(0.5, 2.0))  
    return f"{time.ctime()} Temp: 30°C"

async def get_humidity() :
    await asyncio.sleep(random.uniform(0.5, 2.0))  
    return f"{time.ctime()} Humidity: 60%"  

async def get_weather_api() :
    await asyncio.sleep(random.uniform(0.5, 2.0))  
    return f"{time.ctime()} Weather: Sunny"

async def main():
    start = time.time()
    tasks = [
        asyncio.create_task(get_temperature()),
        asyncio.create_task(get_humidity()),
        asyncio.create_task(get_weather_api())
    ]
    done = set()
    while len(done) < len(tasks):
        finished, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in finished:
            if task not in done:
                print(task.result())
                done.add(task)
    end = time.time()  
    print(f"All tasks completed in {end - start:.2f} seconds.")
asyncio.run(main())