import requests
import time
import asyncio
import httpx

async def fetch(name) :
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    
    async with httpx.AsyncClient() as client :
        response = await client.get(url)
        data = response.json()
        print(f"Name : {data['name'].title()}")
        print(f"ID   : {data['id']} ") 
        print(f"Type : {[t['type']['name'] for t in data['types']]}")

async def main() :
    start = time.time()
    await fetch("pikachu")
    end = time.time()
    print("Total Time :", round(end - start,2), "seconds")

asyncio.run(main())
