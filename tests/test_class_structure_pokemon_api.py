import pytest
import requests


# ------------------------------------------
# This API file is about having passing test using basic OOP structure
# ------------------------------------------

class Pokemon:
    def __init__(self, pokemon_name, pokemon_type):
        self.__pokemon_name = pokemon_name
        self.__pokemon_type = pokemon_type

    @property
    def get_pokemon_name(self):
        return self.__pokemon_name

    @property
    def get_pokemon_type(self):
        return self.__pokemon_type


def api_call(pokemon_name):
    # ARRANGE
    ENDPOINT = 'https://pokeapi.co/api/v2/pokemon/'
    url = f'{ENDPOINT}{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    assert response.status_code == 200
    return body


def test_pokemon():
    # ARRANGE
    # Use Parametrize to create multiple instances of the Pokemon class?
    pokemon = Pokemon("squirtle", "water")

    # ACT
    pokemon_api_call = api_call(pokemon.get_pokemon_name)

    # ASSERT
    #update
    assert pokemon_api_call["name"] == pokemon.get_pokemon_name
    assert pokemon_api_call["types"][0]["type"]["name"] == pokemon.get_pokemon_type
