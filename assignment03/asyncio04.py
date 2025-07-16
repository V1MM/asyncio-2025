# Starting task
import asyncio

async def greet() :
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(greet()) #Create and Run Event loop

#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(greet())
# loop.close()