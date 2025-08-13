import asyncio, time

async def worker_long() :
    print(f"{time.ctime()} Worker Long is running...")

    try :
        await asyncio.sleep(5)  # Simulate a long-running task
        print(f"{time.ctime()} Worker Long completed.")
    except asyncio.CancelledError:
        print(f"{time.ctime()} Worker Long was cancelled.")

async def main():
    print(f"{time.ctime()} Main is running...")
    asyncio.create_task(worker_long())  
    await asyncio.sleep(1)  
    print(f"{time.ctime()} Main is completed.")

asyncio.run(main())