import time
import random
import requests as requests
import httpx
import asyncio
from flask import Blueprint, render_template, current_app

async_bp =Blueprint("async",__name__)

#Fetch pokemon by url
async def get_pokemon(client, url):
    response = await client.get(url)
    print(f"{time.ctime()} - get {url}")
    return response.json()


#Fetch mutiple pokemon
async def get_pokemons() :
    NUMBER_OF_POKEMON = current_app.config["NUMBER_OF_POKEMON"]

    rand_list = []
    for i in range(NUMBER_OF_POKEMON) :
        rand_list.append(random.randint(1,100))
    
    # pokemon_data = []
    # for number in rand_list :
    #     url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    #     pokemon_json = get_pokemon(url)
    #     pokemon_data.append(pokemon_json)
    urls = [f'https://pokeapi.co/api/v2/pokemon/{number}' for number in rand_list]
    async with httpx.AsyncClient() as client:
        task = [get_pokemon(client,url) for url in urls]    
        result = await asyncio.gather(*task)
    return result

@async_bp.route('/')
async def home():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()

    print(f'{time.ctime()} - Get {len(pokemons)} pokemon. Time taken : {end_time-start_time} seconds')

    return render_template('async.html'
                           , title="Pokemon Asynchronous Flask"
                           , heading="Pokemon Asynchronous Version"
                           , pokemons=pokemons
                           , end_time=end_time
                           , start_time=start_time)

