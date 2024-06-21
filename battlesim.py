# Battle Simulator

import demage
import pokemon

class Battle:
    def __init__(self, p1: pokemon.Pokémon, p2: pokemon.Pokémon):
        self.p1 = p1
        self.p2 = p2
        self.current_pokemon = self.p1

    def switch_pokemon(self, new_pokemon: pokemon.Pokémon):
        pass

    def round(self, moveType: str):
        attackerType1 = self.current_pokemon.type1
        attackerType2 = self.current_pokemon.type2
        foeType1 = self.p2.type1
        foeType2 = self.p2.type2