# Create 2 Tasks with High-Level API
import asyncio
import time

async def dowload_image(name, delay) :
    print(f'{name} Downloading...')
    await asyncio.sleep(delay)
    print(f'{name} Finish!')

async def main():
    print(f"{time.ctime()} main coroutine started")
    started_tasks = [asyncio.create_task(dowload_image(i,i)) for i in range(2,-1,-1)]

    await asyncio.sleep(0.1)
    for task in started_tasks :
        await task 

asyncio.run(main() )
                                 
