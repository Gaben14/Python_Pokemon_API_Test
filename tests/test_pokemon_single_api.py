import pytest
import requests


# ------------------------------------------
# Passing tests
# ------------------------------------------


@pytest.mark.valid_test
@pytest.mark.pikachu
def test_pikachu():
    # ARRANGE
    pokemon_name = "pikachu"
    pokemon_type = "electric"
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200
    assert body["name"] == pokemon_name
    assert body["types"][0]["type"]["name"] == pokemon_type


@pytest.mark.valid_test
@pytest.mark.bulbasaur
def test_bulbasaur():
    # ARRANGE
    pokemon_name = "bulbasaur"
    pokemon_type = "grass"
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200
    assert body["name"] == pokemon_name
    assert body["types"][0]["type"]["name"] == pokemon_type


@pytest.mark.valid_test
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

@pytest.mark.valid_test
@pytest.mark.charmander
def test_charmander():
    # ARRANGE
    pokemon_name = "charmander"
    pokemon_type = "fire"
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200
    assert body["name"] == pokemon_name
    assert body["types"][0]["type"]["name"] == pokemon_type
