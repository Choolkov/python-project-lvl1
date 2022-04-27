"""Progression-game logic."""

from random import choice, randint

MIN_LENGHT = 5


def get_rules() -> str:
    """
    Return rules of the game.

    Returns:
        str
    """
    return 'What number is missing in the progression?'


def sequence_generator(
    max_start: int = 30, max_step: int = 5, max_lenght: int = 15,
) -> list:
    """
    Generate sequence of integers with random parameters.

    Args:
        max_start: maximal start number
        max_step: maximal step size
        max_lenght: maximal lenght of sequence

    Returns:
        list

    """
    start = randint(1, max_start)
    step = randint(1, max_step)
    stop = start + randint(MIN_LENGHT, max_lenght) * step
    return list(range(start, stop, step))


def get_round() -> tuple:
    """
    Return round for progression-game.

    Returns:
        tuple: question and right answer
    """
    sequence = list(map(str, sequence_generator()))
    hidden_index = choice(range(len(sequence)))
    right_answer = sequence[hidden_index]
    sequence[hidden_index] = '..'
    return (' '.join(sequence), right_answer)
