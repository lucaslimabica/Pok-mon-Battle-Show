# Instantiate the Pokémon Classes

class Pokémon:
    def __init__(self, specie: str, type1: str, type2: str = None, nickname: str = None):
        self.specie = specie
        self.type1 = type1
        self.type2 = type2
        self.nickname = nickname

    def __str__(self):
        return f"{self.nickname or self.specie} ({self.type1}/{self.type2})"
    

pokemon_dict = {
    "Bulbasaur": {"species": "Bulbasaur", "type1": "Grass", "type2": "Poison", "nickname": "Bulba"},
    "Charmander": {"species": "Charmander", "type1": "Fire", "type2": None, "nickname": "Char"},
    "Squirtle": {"species": "Squirtle", "type1": "Water", "type2": None, "nickname": "Squirt"},
    "Pikachu": {"species": "Pikachu", "type1": "Electric", "type2": None, "nickname": "Pika"},
    "Jigglypuff": {"species": "Jigglypuff", "type1": "Normal", "type2": "Fairy", "nickname": "Jiggly"},
    "Meowth": {"species": "Meowth", "type1": "Normal", "type2": None, "nickname": "Meow"},
    "Machop": {"species": "Machop", "type1": "Fighting", "type2": None, "nickname": "Macho"},
    "Abra": {"species": "Abra", "type1": "Psychic", "type2": None, "nickname": None},
    "Geodude": {"species": "Geodude", "type1": "Rock", "type2": "Ground", "nickname": "Geo"},
    "Eevee": {"species": "Eevee", "type1": "Normal", "type2": None, "nickname": "Eevee"}
}

for pokemon_name, pokemon_data in pokemon_dict.items():
    specie = pokemon_data["species"]
    type1 = pokemon_data["type1"]
    type2 = pokemon_data["type2"]
    nickname = pokemon_data.get("nickname")
    p = Pokémon(specie, type1, type2, nickname)
    print(p)
