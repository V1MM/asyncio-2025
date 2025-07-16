# Check if a Task is Done
import asyncio

async def simple_task() :
    await asyncio.sleep(1)
    return "Finish"

async def main() :
    task = asyncio.create_task(simple_task() )
    print("before await : ", task.done() ) # Not finish
    await task
    print("after await", task.done()) # Finish

asyncio.run(main())