import asyncio
import time

#SuperMarket simulation
# • Supermarket simulation using Python asyncio to create a multi-customer, multi-cashier system.
# • There are three customers who purchase products:
# • Alice buys apples, bananas, and milk
# • Bob buys bread and cheese
# • Charlie buys eggs, juice, and butter
# • There are two cashiers who process customer orders:
# • Cashier-1: takes 1 second per item
# • Cashier-2: takes 2 seconds per item
# • Rules:
# • Each customer's order is a single task
# • Each cashier retrieves tasks from the queue one at a time
# • Cashiers can work in parallel, but each customer processes one customer at a time
# • The system must wait for all customers to be paid before closing the store

async def customer(name, items, queue):
    print(f'{time.ctime()} : [{name}] finish shopping : {items}')
    await queue.put((name, items))
    
async def cashier(name, process_time, queue):
    while True:
        customer_info = await queue.get()
        if customer_info is None:
            break
        customer_name, items = customer_info
        print(f'{time.ctime()} : [{name}] : processing {customer_name} with orders {items}')
        for item in items:
            await asyncio.sleep(process_time)
            print(f'{time.ctime()} >>>> {name} : processed {item} for {customer_name}')
        print(f'{time.ctime()} : [{name}] finished {customer_name}')
        queue.task_done()
    print(f'{time.ctime()} : [{name}] closing down')

async def main():
    # Create a queue for customer orders
    order_queue = asyncio.Queue()

    # List of customers and their shopping items
    customer_list = [
        ("Alice", ["Apple", "Banana", "Milk"]),
        ("Bob", ["Bread", "Cheese"]),
        ("Charlie", ["Eggs", "Juice", "Butter"])
    ]

    # List of cashiers and their processing times per item
    cashier_list = [
        ("Cashier-1", 1),
        ("Cashier-2", 2)
    ]

    # Start customer tasks: each customer puts their order in the queue
    customer_tasks = [
        asyncio.create_task(customer(name, items, order_queue))
        for name, items in customer_list
    ]

    # Start cashier tasks: each cashier processes orders from the queue
    cashier_tasks = [
        asyncio.create_task(cashier(name, process_time, order_queue))
        for name, process_time in cashier_list
    ]

    # Wait for all customers to finish shopping
    await asyncio.gather(*customer_tasks)

    # Wait until all orders have been processed
    await order_queue.join()

    # Signal cashiers to stop by putting None in the queue
    for _ in cashier_list:
        await order_queue.put(None)

    # Wait for all cashiers to finish
    await asyncio.gather(*cashier_tasks)

    print(f'{time.ctime()} [Main] Supermarket is closed!')

asyncio.run(main())
