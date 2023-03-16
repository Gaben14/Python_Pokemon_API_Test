import requests

def get_squirtle():
    # ARRANGE
    url = 'https://pokeapi.co/api/v2/pokemon/squirtle'

    # ACT
    response = requests.get(url)
    body = response.json()
    print(body["types"][0]["type"]["name"])
    # [{'slot': 1, 'type': {'name': 'water', 'url': 'https://pokeapi.co/api/v2/type/11/'}}]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_squirtle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
