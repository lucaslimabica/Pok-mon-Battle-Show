# Battle Simulator

import demage
import pokemon
import random

class Battle:
    def __init__(self, p1: pokemon.Pokémon, p2: pokemon.Pokémon):
        self.p1 = p1
        self.p2 = p2
        self.current_pokemon = self.p1
        self.current_round = 1

    def switch_pokemon(self, new_pokemon: pokemon.Pokémon):
        pass

    def knockout(self):
        hp = self.p2.stats[0]
        if hp <= 0:
            return True
        else:
            return False

    def round(self, moveType: str, power: int, moveName: str, moveAccuracy: float):
        foeType1 = self.p2.type1
        foeType2 = self.p2.type2

        stab = demage.isSTAB(moveType, self.current_pokemon.types())
        advantage = demage.calculateAdvantage(moveType, [foeType1, foeType2])
        damage = demage.calculateDamage(
            self.current_pokemon.level,
            power,
            self.current_pokemon.stats[1],
            self.p2.stats[2],
            moveType,
            self.current_pokemon.types(),
            self.p2.types(),
        )

        # Accuracy check
        chance = random.randint(1, 100) <= moveAccuracy
        if chance:
            # Description of the move
            print(f"{self.current_pokemon.nickname} used {moveName}!")
            print("It's a STAB move!") if stab != 1 else None
            print("Super Effective!") if advantage != 1 and advantage is not None else None
            print(f"{self.p2.nickname} took {damage} damage!")
            self.p2.stats[0] -= damage
        else:
            print(f'{self.current_pokemon.nickname} used {moveName}, but it missed!')
        
        if self.knockout():
            print(f"{self.p2.nickname} fainted!")
        
        self.current_round += 1



p1 = pokemon.Pokémon("Bulbasaur", "Grass", "Poison", stats=[45, 49, 49, 45, 65,])
p2 = pokemon.Pokémon("Charmander", "Fire", "Rock", "Char")
battle = Battle(p1, p2)
for i in range(10):
    battle.round("water", 60, "Bubbles", 90)