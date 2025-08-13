import asyncio, time

async def worker_ok():
    print(f"{time.ctime()} Worker OK is running...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Worker OK completed.")

async def main():
    asyncio.create_task(worker_ok()) #fire and forget
    await asyncio.sleep(2)  # Allow time for the worker to complete

asyncio.run(main())