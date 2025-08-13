import asyncio

async def task_ok(n):
    await asyncio.sleep(n)
    return f"OK after {n} seconds"

async def task_error(n):
    await asyncio.sleep(n)
    raise ValueError(f"Error after {n} seconds")

async def demo_wait():
    print("\n=== wait: return values ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_ok(2))}
    done , pending = await asyncio.wait(tasks)
    print("Done:", [t.result() for t in done])
    print("Pending:", pending)

    print("\n=== wait : handle erros manually ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_error(2))}
    done, pending = await asyncio.wait(tasks)
    for t in done:
        if t.exception():
            print("Caught an error:", t.exception())
        else:
            print("Result:", t.result())
    
    print("\n=== wait: FIRST_COMPLETED === ")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_error(3))}
    done , pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("First Done:", [t.result() for t in done])
    print("Still Pending:", len(pending), "tasks(s)")

async def main():
    await demo_wait()

asyncio.run(main())
