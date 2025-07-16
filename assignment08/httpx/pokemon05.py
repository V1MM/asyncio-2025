import time
import asyncio
import httpx

def sort_key(data):
    return data["base_experience"]

async def fetch(pokemon_names):
    async with httpx.AsyncClient() as client:  
        tasks = []

        for name in pokemon_names:
            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            tasks.append(client.get(url))  

        responses = await asyncio.gather(*tasks) 
        all_data = []
        for response in responses:
            data = response.json()
            all_data.append(data)
        sorted_data = sorted(all_data, key=sort_key, reverse=True)

        for data in sorted_data:
           print(f"{data['name']:<15} → ID: {data['id']:<5}, Base XP: {data['base_experience']:<5}")

async def main():
    names = ['pikachu', 'bulbasaur', 'charmander', 'squirtle', 'eevee',
             'snorlax', 'gengar', 'mewtwo', 'psyduck', 'jigglypuff']
    
    start = time.time()
    await fetch(names)
    end = time.time()
    print("Total Time:", round(end - start, 2), "seconds")

asyncio.run(main())
