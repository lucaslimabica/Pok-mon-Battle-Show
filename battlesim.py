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

        print(f"A wild {self.p2.nickname} appeared!")
        print(f"{self.p1.nickname} vs. {self.p2.nickname}")
        print("-=" * 12)

    def switch_pokemon(self):
        if self.current_pokemon == self.p1:
            self.current_pokemon = self.p2
        else:
            self.current_pokemon = self.p1

    def knockout(self):
        hp = self.p2.stats[0]
        if hp <= 0:
            return True
        else:
            return False

    def round(self, move: dict):
        try:
            moveType = move['moveType']
            power = move['power']
            moveName = move['moveName']
            moveAccuracy = move['moveAccuracy']
        except KeyError:
            raise ValueError("Move must contain moveType, power, moveName, and moveAccuracy.")
        print(f"------ Round {self.current_round} ------")
        
        if self.current_pokemon == self.p1:
            self.foe = self.p2
        else:
            self.foe = self.p1
        
        foeType1 = self.foe.type1
        foeType2 = self.foe.type2

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
            if advantage > 1:
                print("Super Effective!")
            elif advantage < 1 and advantage > 0:
                print("Not very Effective!")
            print(f"{self.foe.nickname} took {damage} damage!")
            self.foe.stats[0] -= damage
        else:
            print(f'{self.current_pokemon.nickname} used {moveName}, but it missed!')
        
        if self.knockout():
            print(f"{self.foe.nickname} fainted!")
            self.current_pokemon.get_xp(amount=self.gain_exp())
            self.batlle_end()
        
        self.current_round += 1
        self.switch_pokemon()

    def batlle_end(self):
        return True

    def gain_exp(self) -> int:
        """
        EXP = (a X b X L X s) / (7 X p X t)
        a = Base experience value for each specie
        b = Level of the fainted Pokémon
        L = Level of the current Pokémon
        s = Number of the Pokém that participated in the battle and still alive
        p = Number of Pokémon in the party
        t = Multiplier, 1 for normal Pokémon and 1.5 for traded Pokémon  
        """
        a = 64
        b = self.foe.level
        lv = self.current_pokemon.level
        s = 1
        p = 1
        t = 1
        exp = (a * b * lv * s) / (7 * p * t)
        return int(exp)


moves = [{"moveName": "Tackle", "power": 40, "moveType":  "Normal", "moveAccuracy": 100},
         {"moveName": "Ember", "power": 40, "moveType": "fire", "moveAccuracy": 100},
         {"moveName": "Flamethrower", "power": 60, "moveType": "fire","moveAccuracy": 90}]

p1 = pokemon.Pokémon("Bulbasaur", "Grass", "Poison", stats=[45, 67, 49, 45, 65,], level=1)
p2 = pokemon.Pokémon("Charmander", "Fire", "Rock", nickname="Flame", stats=[1, 49, 39, 41, 79,], level=15)
battle = Battle(p1, p2)
battle.round(move=random.choice(moves))
print(p1.pokemon_info())
