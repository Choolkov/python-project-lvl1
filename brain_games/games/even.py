"""Even-game logic."""

from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """
    Predicate for checking integers for parity.

    Args:
        number: integer

    Returns:
        bool

    """
    return not number % 2


def get_round() -> tuple:
    """
    Return round for even-game.

    Returns:
        tuple: question and right answer
    """
    number = randint(1, 100)
    right_answer = 'yes' if is_even(number) else 'no'
    return str(number), right_answer
