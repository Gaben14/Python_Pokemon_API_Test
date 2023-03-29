import pytest
import requests


# ------------------------------------------
# This API file is about having passing test using basic OOP structure
# ------------------------------------------

class Pokemon:
    def __init__(self, pokemon_name, pokemon_type):
        self.pokemon_name = pokemon_name
        self.pokemon_type = pokemon_type

@pytest.mark.squirtle
def test_squirtle():
    # ARRANGE
    pokemon_name = "squirtle"
    pokemon_type = "water"
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200
    assert body["name"] == pokemon_name
    assert body["types"][0]["type"]["name"] == pokemon_type

