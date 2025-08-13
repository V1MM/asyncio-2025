import asyncio, time 
async def say_after(delay, msg):
    if msg == 'World':
        print(f"{time.ctime()} {msg} is blocking...... {delay} second.")
        time.sleep(delay)
    else:
        print(f"{time.ctime()} {msg} is not blocking...... {delay} second.")
        await asyncio.sleep(delay)

async def main():
    task1 = asyncio.create_task(say_after(1, 'Hello'))
    task2 = asyncio.create_task(say_after(5, 'World'))
    await task1
    await task2

asyncio.run(main())
print(f"{time.ctime()} All tasks completed.")

