import asyncio
import httpx

async def fetch_ability_list():
    url = "https://pokeapi.co/api/v2/ability?limit=10"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return data["results"]

async def fetch_ability_detail(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    ability_name = f"{data['name']:<15}"
    pokemon_list = [countname['pokemon']['name'] for countname in data["pokemon"]]

    results = f'{ability_name:<15} > {len(pokemon_list):<3} Pokemon { ",".join(pokemon_list[:5])} '
    
    return results

async def main():
    ability_list = await fetch_ability_list()
    tasks = [fetch_ability_detail(item["url"]) for item in ability_list]
    results = await asyncio.gather(*tasks)
    for line in results:
        print(line) 

asyncio.run(main())

