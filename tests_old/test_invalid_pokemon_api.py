import pytest
import requests


# ------------------------------------------
# Failing tests - 2023.03.20 - Rewrite this file with the pytest.raises solution?
# ------------------------------------------


@pytest.mark.invalid_test
@pytest.mark.pikachard
def test_pikachard():
    # ARRANGE
    url = 'https://pokeapi.co/api/v2/pokemon/pikachard'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200


@pytest.mark.invalid_test
@pytest.mark.raimundo
def test_raimundo():
    # ARRANGE
    url = 'https://pokeapi.co/api/v2/pokemon/raimundo'

    # ACT
    response = requests.get(url)
    body = response.json()

    # ASSERT
    assert response.status_code == 200
