# example of using an asyncio queue without blocking
from random import random
import asyncio


async def producer(queue) :
    print('Producer : running')
    for i in range(10) :
        value = i
        sleep_time = random()
        print(f'> Producer sleeping for {sleep_time:.2f} seconds')
        await asyncio.sleep(sleep_time)
        print(f'> Producer put {value}')
        # add to the queue 
        await queue.put(value)
    # send an all done signal   
    await queue.put(None)
    print('Producer : done')

async def consumer(queue) :
    print('Consumer : running')
    while True :
        try : 
            item = queue.get_nowait()
        except asyncio.QueueEmpty :
            print('Consumer : queue empty, waiting a while')
            await asyncio.sleep(0.5)
            continue
        if item is None :
            break
        print(f'\t> Consumer got {item}')
    print('Consumer : done')

async def main() :
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
