import time
import random
import requests as requests
from flask import Blueprint, render_template, current_app

sync_bp =Blueprint("sync",__name__)

#Fetch pokemon by url
def get_pokemon(url) :
    response = requests.get(url)
    print(f"{time.ctime()} - get {url} ")
    return response.json()

#Fetch mutiple pokemon
def get_pokemons() :    
    NUMBER_OF_POKEMON = current_app.config["NUMBER_OF_POKEMON"]

    rand_list = []
    for i in range(NUMBER_OF_POKEMON) :
        rand_list.append(random.randint(1,100))
    
    pokemon_data = []
    for number in rand_list :
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)
        pokemon_data.append(pokemon_json)
    return pokemon_data

@sync_bp.route('/')
def home():
    start_time = time.perf_counter()
    pokemons = get_pokemons()
    end_time = time.perf_counter()

    print(f'{time.ctime()} - Get {len(pokemons)} pokemon. Time taken : {end_time-start_time} seconds')

    return render_template('sync.html'
                           , title="Pokemon Synchronous Flask"
                           , heading="Pokemon Synchronous Version"
                           , pokemons=pokemons
                           , end_time=end_time
                           , start_time=start_time)

