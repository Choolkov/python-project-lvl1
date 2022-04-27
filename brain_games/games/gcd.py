"""GCD-game logic."""

from random import randint

MAX_NUMBER = 30


def get_rules() -> str:
    """
    Return rules of the game.

    Returns:
        str
    """
    return 'Find the greatest common divisor of given numbers.'


def gcd(value1: int, value2: int) -> int:
    """
    Return GCD of two numbers.

    Args:
        value1: firts value
        value2: second value

    Returns:
        int

    """
    return gcd(value2, value1 % value2) if value2 else value1


def get_round():
    """
    Return round for gcd-game.

    Returns:
        tuple: question and right answer
    """
    number1 = randint(1, MAX_NUMBER)
    number2 = randint(1, MAX_NUMBER)
    numbers = '{0} {1}'.format(number1, number2)
    return (numbers, str(gcd(number1, number2)))
