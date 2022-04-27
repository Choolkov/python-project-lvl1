"""Even-game logic."""

from random import randint


def get_rules() -> str:
    """
    Return rules of the game.

    Returns:
        str
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round() -> tuple:
    """
    Return round for even-game.

    Returns:
        tuple: question and right answer
    """
    number = randint(1, 100)
    right_answer = 'no' if number % 2 else 'yes'
    return (str(number), right_answer)
