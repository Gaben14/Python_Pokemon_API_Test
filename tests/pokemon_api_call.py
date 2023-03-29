import requests

def api_call(pokemon_name):
    # ARRANGE
    endpoint = 'https://pokeapi.co/api/v2/pokemon/'
    url = f'{endpoint}{pokemon_name}'

    # ACT
    response = requests.get(url)
    body = response.json()

    assert response.status_code == 200
    return body