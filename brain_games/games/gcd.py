"""GCD logic."""

from random import randint

from brain_games.engine import ROUNDS_AMOUNT, game

min_number = 1
max_number = 20


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


def gcd_game():
    """GCD game."""
    rules = 'Find the greatest common divisor of given numbers.'
    rounds = []
    for _ in range(ROUNDS_AMOUNT):
        number1 = randint(1, max_number)
        number2 = randint(1, max_number)
        numbers = '{0} {1}'.format(number1, number2)
        rounds.append((numbers, str(gcd(number1, number2))))
    game(rules, rounds)


if __name__ == '__main__':
    gcd_game()
