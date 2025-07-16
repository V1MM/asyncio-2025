import time
import asyncio
import httpx

async def fetch(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json() 
        return data["name"], data["id"], [t['type']['name'] for t in data['types']] 

async def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle", "snorlax"]
    start = time.time()

    tasks = [fetch(name) for name in pokemon_names]
    results = await asyncio.gather(*tasks)

    for name, id, t in results:
        print(f"{name} → ID: {id} Types : {t}")

    end = time.time()
    print("Total Time:", round(end - start, 2), "seconds")

asyncio.run(main())
