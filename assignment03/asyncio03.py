# example of creating an event loop
import asyncio
async def say_after(delay, msg) :
    await asyncio.sleep(delay) # What come before await function IS NOT ASYNC 
    print(msg)
    
async def main() :
    task1 = asyncio.create_task(say_after(1,"hello"))
    task2 = asyncio.create_task(say_after(2,"world"))

    await task2
    await task1
    

asyncio.run(main())