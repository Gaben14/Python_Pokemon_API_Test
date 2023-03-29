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