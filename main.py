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
    after divide by 2 and sum 2.
    """
    level = 1 if level < 1 else level
    critical_value = isCritical()
    return int((level * 2 * critical_value) // 2 + 2)


def powerAD(power: int, attack: int, defense: int) -> int:
    """
    Returns the damage done by the attacker based on the given power, attack, and defense.
    The damage is calculated by multiplying the power by the divison of attack value by the defense value.
    """
    for value in (power, attack, defense):
        if value <= 0:
            value = 1

    attack_value = attack
    defense_value = defense
    power_value = power
    return int(power_value * (attack_value / defense_value))
