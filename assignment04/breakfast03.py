# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():  # 1
    print("coffee: prepare ingridients")
    await asyncio.sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)  # 2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():  # 1
    print("eggs: prepare ingridients")
    await asyncio.sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)  # 2: pause, another tasks can be run
    print("eggs: ready")


async def main() :
    start = time()
    task1 = asyncio.create_task( make_coffee() )
    task2 = asyncio.create_task( fry_eggs() )

    await task1
    await task2

    Time = time()-start
    
    print(f"breakfast is ready in {f"{Time:.2f}"} secs.")

asyncio.run(main())