import pytest
import requests

# ------------------------------------------
# API key function - To keep the DRY principle
# ------------------------------------------

pokemons = [("squirtle", "water"), ("bulbasaur", "grass"), ("charmander", "fire"), ("pikachu", "electric")]


@pytest.mark.valid_test
@pytest.mark.parametrize('pokemon_name, pokemon_type', pokemons)
def test_pokemon(pokemon_name, pokemon_type):
    """In this function we want to compare the value (name) of the PokeApi
    with the given Pokemon name and also to test the API connection

    """
    # ARRANGE
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200
    assert body["name"] == pokemon_name
    assert body["types"][0]["type"]["name"] == pokemon_type
