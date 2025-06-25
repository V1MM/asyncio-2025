# Create 2 Tasks with High-Level API
import asyncio

async def dowload_image(name, delay) :
    print(f'{name} Downloading...')
    await asyncio.sleep(delay)
    print(f'{name} Finish!')

async def main():
    task1 = asyncio.create_task(dowload_image("Image 1", 5))
    task2 = asyncio.create_task(dowload_image("Image 2", 3))

    await task1
    await task2

asyncio.run(main() )
                                 
