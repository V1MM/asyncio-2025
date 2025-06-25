# get result
import asyncio

async def simple_task() :
    await asyncio.sleep(1)
    return "Finish"

async def main() :
    task = asyncio.create_task(simple_task())
    await task
    print("Output Task : ", task.result())

asyncio.run(main())