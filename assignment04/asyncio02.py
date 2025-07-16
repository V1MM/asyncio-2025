# Create 1 Task with High-Level API
import asyncio

async def do_something() :
    print("working...")
    await asyncio.sleep(2)
    print("done...")

async def main():
    task = asyncio.create_task(do_something())
    await task # wait untill task dones 

asyncio.run(main())