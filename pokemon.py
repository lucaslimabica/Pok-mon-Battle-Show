# Instantiate the Pokémon Classes

class Pokémon:
    def __init__(self, specie: str, type1: str, type2: str = None, nickname: str = None, level: int = 1):
        self.__specie = specie
        self.__type1 = type1
        self.__type2 = type2
        self.__nickname = nickname
        self.__level = level
        self.__xp = 0

    @property
    def specie(self):
        return self.__specie

    @specie.setter
    def specie(self, value):
        self.__specie = value

    @property
    def type1(self):
        return self.__type1

    @type1.setter
    def type1(self, value):
        self.__type1 = value

    @property
    def type2(self):
        return self.__type2

    @type2.setter
    def type2(self, value):
        self.__type2 = value

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        self.__nickname = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if value < 1:
            raise ValueError("Level must be at least 1.")
        self.__level = value

    @property
    def xp(self):
        return self.__xp

    @xp.setter
    def xp(self, value):
        if value < 0:
            raise ValueError("XP cannot be negative.")
        self.__xp = value

    def get_xp(self, amount: int):
        self.xp += amount
        if self.xp >= self.level * 100:
            self.level_up()
            self.xp -= self.level * 100

    def level_up(self):
        self.level += 1
        print(f"{self.nickname or self.specie} leveled up to Lv.{self.level}!")

    def __str__(self):
        return f"{self.nickname or self.specie} Lv.{self.level} ({self.type1}/{self.type2})"
    

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

pokes = []

for pokemon_name, pokemon_data in pokemon_dict.items():
    specie = pokemon_data["species"]
    type1 = pokemon_data["type1"]
    type2 = pokemon_data["type2"]
    nickname = pokemon_data.get("nickname")
    p = Pokémon(specie, type1, type2, nickname)
    pokes.append(p)
    print(p)

print(f"{pokes[7]} defeated {pokes[3]} and gained 250 XP")
pokes[7].get_xp(250)
print(f"{pokes[7].nickname or pokes[7].specie} now has {pokes[7].xp} XP")
