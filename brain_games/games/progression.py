"""Progression-game logic."""

from random import choice, randint

RULES = 'What number is missing in the progression?'


def get_random_progression(
    max_initial_term: int = 30,
    max_common_difference: int = 5,
    min_lenght: int = 5,
    max_lenght: int = 15,
) -> list:
    """
     Return arithmetic progression of integers with random parameters.

    Args:
        max_initial_term: maximal initial term
        max_common_difference: maximal common diffirence
        min_lenght: minimal lenght of the progression
        max_lenght: maximal lenght of the progression

    Returns:
        list

    """
    start = randint(1, max_initial_term)
    step = randint(1, max_common_difference)
    stop = start + randint(min_lenght, max_lenght) * step
    return list(range(start, stop, step))


def get_round() -> tuple:
    """
    Return round for progression-game.

    Returns:
        tuple: question and right answer
    """
    sequence = list(map(str, get_random_progression()))
    hidden_index = choice(range(len(sequence)))
    right_answer = sequence[hidden_index]
    sequence[hidden_index] = '..'
    return ' '.join(sequence), right_answer
