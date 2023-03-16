import pytest
import requests

# ------------------------------------------
# API key function - To keep the DRY principle
# ------------------------------------------


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


# ------------------------------------------
# Testing different Pokemon API calls
# ------------------------------------------
@pytest.mark.squirtle
def test_squirtle():
    test_pokemon("squirtle", "water")

@pytest.mark.bulbasaur
def test_bulbasaur():
    test_pokemon("bulbasaur", "grass")


@pytest.mark.charmander
def test_charmander():
    test_pokemon("charmander", "fire")


@pytest.mark.pikachu
def test_pikachu():
    test_pokemon("pikachu", "electric")
