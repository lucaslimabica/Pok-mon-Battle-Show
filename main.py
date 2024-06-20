# Damage Calculator Gen I
import random


def isCritical():
    """
    Returns a random integer, 1 or 2 to determine if a hit is critical.
    A critical hit occurs with a 5% chance.
    """
    chance = random.randint(1, 100) <= 5
    if chance:
        return 2
    else:
        return 1


def levelValue(level: int) -> int:
    """
    Returns the operation value based on the given level.
    The level value is calculated by multiplying the level by 2 and by the critical value,
    after divide by 5 and sum 2.
    """
    level = 1 if level < 1 else level
    critical_value = isCritical()
    return int((level * 2 * critical_value) / 5 + 2)


def powerAD(power: int, attack: int, defense: int) -> int:
    """
    Returns the damage done by the attacker based on the given power, attack, and defense.
    The damage is calculated by multiplying the power by the divison of attack value,
    by the defense value and then by 50.
    """
    for value in (power, attack, defense):
        if value <= 0:
            value = 1
    if attack > 255 or defense > 255:
        attack_value = 255 / 4
        defense_value = 255 / 4

    attack_value = attack
    defense_value = defense
    power_value = power
    return int(power_value * (attack_value / defense_value))


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

def calculateAdvantage(attackType: str, pokemonType1: str, pokemonType2: str = None) -> float:
    """
    Returns the advantage factor based on the given attack type,
    and the types of the foe Pokémon.
    The advantage factor is calculated by multiplying the value of the first advantages
    for the second one of the foe Pokémon.
    """
    type_advantages = {
        "fire": ["grass", "bug", "ice"],
        "water": ["fire", "ground", "rock"],
        "grass": ["water", "ground", "rock"]
    }

    # Verifica se pokemonType2 foi fornecido
    if pokemonType2 is None:
        if pokemonType1 in type_advantages.get(attackType, []):
            return 2
        else:
            return 1
    else:
        if pokemonType1 in type_advantages.get(attackType, []) and pokemonType2 in type_advantages.get(attackType, []):
            return 4
        elif pokemonType1 in type_advantages.get(attackType, []):
            return 2
        elif pokemonType2 in type_advantages.get(attackType, []):
            return 2
        else:
            return 1
