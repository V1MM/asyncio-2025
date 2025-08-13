import asyncio, time

async def worker_error():
    print(f"{time.ctime()} Worker Error is running...")
    await asyncio.sleep(1)
    raise ValueError("An error occurred in Worker Error.") # ERROR

async def main():
    asyncio.create_task(worker_error())  
    await asyncio.sleep(2)  

asyncio.run(main())