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
    
def levelValue(level):
    """
    Returns the operation value based on the given level.
    The level value is calculated by multiplying the level by 2 and by the critical value,
    after divide by 2 and sum 2.
    """
    critical_value = isCritical()
    return (level * 2 * critical_value) // 2 + 2