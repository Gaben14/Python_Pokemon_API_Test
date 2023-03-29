import pytest
import requests
from pokemon import Pokemon
from pokemon_api_call import api_call

# ------------------------------------------
# This API test file is about having passing test using basic OOP structure
# ------------------------------------------
pokemons = [("squirtle", "water"), ("bulbasaur", "grass"), ("charmander", "fire"), ("pikachu", "electric")]


@pytest.mark.pokemon_structure_test
@pytest.mark.parametrize('pokemon_name, pokemon_type', pokemons)
def test_pokemon(pokemon_name, pokemon_type):
    # ARRANGE
    # Use Parametrize to create multiple instances of the Pokemon class?
    pokemon = Pokemon(pokemon_name, pokemon_type)

    # ACT
    pokemon_api_call = api_call(pokemon.get_pokemon_name)

    # ASSERT
    # update
    assert pokemon_api_call["name"] == pokemon.get_pokemon_name
    assert pokemon_api_call["types"][0]["type"]["name"] == pokemon.get_pokemon_type
