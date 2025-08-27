# example of using an asyncio queue
from random import random
import asyncio

async def producer(queue) :
    print('Producer : running')
    # generate work
    for i in range(10) :
        # generate value
        value = i
        # block to simulate work
        await asyncio.sleep(random())
        # add to the queue
        print(f'> Producer put {value}')
        await queue.put(value)
    # send an all done signal
    await queue.put(None)   
    print('Producer : done') 

async def consumer(queue) :
    print('Consumer : running')
    # consume work
    while True :
        # get a unit of work
        item = await queue.get()
        # check for the all done signal
        if item is None :
            break
        # report a result
        print(f'< Consumer got {item}')
    #all done
    print('Consumer : done')
    
async def main() :
    # create the shared queue
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main())