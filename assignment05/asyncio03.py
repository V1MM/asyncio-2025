# example of waiting for the first task to fail
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')
    # conditionally faill
    if value < 0.1 :
        raise Exception (f'Something bad happend in {arg}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for first tasks to fail or all tasks to complete
    done,pending = await asyncio.wait(tasks,return_when=asyncio.FIRST_EXCEPTION)
    # report results
    print('done')
    # get the first task to complete
    first = done.pop()
    print(first)

#start the asyncio program
asyncio.run(main())