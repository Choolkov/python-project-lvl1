"""Prime-game logic."""

from random import randint

MAX_NUMBER = 50
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """
    Predicate for checking positive integers for prime numbers.

    Args:
        number: integer for check

    Returns:
        bool

    """
    if number < 2:
        return False
    elif number == 2:
        return True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def get_round() -> tuple:
    """
    Return round for prime-game.

    Returns:
        tuple: question and right answer
    """
    number = randint(1, MAX_NUMBER)
    right_answer = 'yes' if is_prime(number) else 'no'
    return str(number), right_answer
