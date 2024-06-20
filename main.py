# Damage Calculator Gen I
import random
from collections import Counter


def isCritical():
    """
    Returns a random integer, 1 or 2 to determine if a hit is critical.
    A critical hit occurs with a 5% chance.
    """
    chance = random.randint(1, 100) <= 5
    return 2 if chance else 1

def levelValue(level: int) -> int:
    """
    Returns the operation value based on the given level.
    The level value is calculated by multiplying the level by 2 and by the critical value,
    after divide by 5 and sum 2.
    """
    level = max(1, level)
    critical_value = isCritical()
    return int((level * 2 * critical_value) / 5 + 2)


def powerAD(power: int, attack: int, defense: int) -> int:
    """
    Returns the damage done by the attacker based on the given power, attack, and defense.
    The damage is calculated by multiplying the power by the divison of attack value,
    by the defense value and then by 50.
    """
    attack = max(1, attack)
    defense = max(1, defense)
    power = max(1, power)
    
    if attack > 255 or defense > 255:
        attack = attack / 4
        defense = defense / 4

    return int(power * (attack / defense))


def calculateParentheses(level: int, power: int, attack: int, defense: int) -> int:
    """
    Returns the value done by the attacker based on the given level, power, attack, and defense.
    The damage is calculated by multiplying the result of the level value by the power AD value
    and divide by 50 and suming 2.
    """
    level_value = levelValue(level)
    damage = powerAD(power, attack, defense)
    return int((level_value * damage) / 50 + 2)

def isSTAB(attackType: str, pokemonType: str):
    """
    Returns 1.5 if the attack type is STAB (Strong Type Attack Bonus),
    and 1 otherwise.
    """
    return 1.5 if attackType == pokemonType else 1

def calculateAdvantage(attackType: str, foeType1: str, foeType2: str = None) -> float:
    """
    Returns the advantage factor based on the given attack type,
    and the types of the foe Pokémon.
    The advantage factor is calculated by multiplying the value of the first advantages
    for the second one of the foe Pokémon.
    
    Parameters:
    attackType (str): The type of the attack.
    foeType1 (str): The primary type of the foe Pokémon.
    foeType2 (str, optional): The secondary type of the foe Pokémon. Defaults to None.

    Returns:
    float: The advantage factor.

    Examples:
    >>> calculateAdvantage("fire", "grass")
    2
    >>> calculateAdvantage("fire", "grass", "bug")
    4
    >>> calculateAdvantage("water", "fire")
    2
    >>> calculateAdvantage("water", "fire", "rock")
    4
    """
    type_advantages = {
        "fire": ["grass", "bug", "ice"],
        "water": ["fire", "ground", "rock"],
        "grass": ["water", "ground", "rock"],
        "bug": ["grass", "psychic", "dark"],
        "ice": ["grass", "ground", "flying", "dragon"],
        "dragon": ["dragon"],
        "ghost": ["ghost", "psychic"],
        "psychic": ["fighting", "poison"],
        "fighting": ["normal", "ice", "rock", "dark", "steel"],
        "dark": ["psychic", "ghost"],
        "steel": ["ice", "rock", "fairy"],
        "fairy": ["fighting", "dragon", "dark"],
        "electric": ["water", "flying"],
        "poison": ["grass", "fairy"],
        "ground": ["fire", "electric", "poison", "rock", "steel"],
        "flying": ["grass", "fighting", "bug"],
        "rock": ["fire", "ice", "flying", "bug"],
        "normal": []
    }

    if foeType2 is None:
        return 2 if foeType1 in type_advantages.get(attackType, []) else 1
    else:
        multiplier = 1
        if foeType1 in type_advantages.get(attackType, []):
            multiplier *= 2
        if foeType2 in type_advantages.get(attackType, []):
            multiplier *= 2
        return multiplier
    

def calculateDamage(level: int, power: int, attack: int, defense: int, attackType: str, pokemonType: str, foeType1: str, foeType2: str = None):
    """
    Returns the damage done by the attacker based on the given level, power, attack, defense,
    attack type, and types of the foe Pokémon.
    
    Parameters:
    level (int): The level of the attacker Pokémon.
    power (int): The power of the attack.
    attack (int): The attack value of the attacker Pokémon.
    defense (int): The defense value of the defender Pokémon.
    attackType (str): The type of the attack.
    foeType1 (str): The primary type of the foe Pokémon.
    foeType2 (str, optional): The secondary type of the foe Pokémon. Defaults to None.
    """
    parentheses_damage = calculateParentheses(level, power, attack, defense)
    advantage_factor = calculateAdvantage(attackType, foeType1, foeType2)
    stab_factor = isSTAB(attackType, pokemonType)
    return int(parentheses_damage * advantage_factor * stab_factor * random.uniform(0.85, 1.00))

# Testing the functions

print("Charizard X Venusaur!")
log = []
for i in range(100):
    x = calculateDamage(50, 95, 100, 85, "fire", "fire", "grass")
    log.append(x)

print(f"Average damage: {sum(log) / len(log)}")
print(f"Minimum damage: {min(log)}")
print(f"Maximum damage: {max(log)}")
couting = Counter(log)
print(f"Most commun amout of damage: {couting.most_common(1)[0]}")
print(f"Least commun amout of damage: {couting.most_common()[-1]}")

print("\nSquirtle X Wartortle!")

log = []

for i in range(100):
    x = calculateDamage(50, 90, 85, 100, "water", "water", "water")
    log.append(x)

print(f"Average damage: {sum(log) / len(log)}")

print(f"Minimum damage: {min(log)}")

print(f"Maximum damage: {max(log)}")

couting = Counter(log)

print(f"Most commun amout of damage: {couting.most_common(1)[0]}")

print(f"Least commun amout of damage: {couting.most_common()[-1]}")

    