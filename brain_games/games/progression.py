"""Progression logic."""

from random import choice, randint

from brain_games.engine import ROUNDS_AMOUNT, game


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
    min_lenght = 5
    start = randint(1, max_start)
    step = randint(1, max_step)
    stop = start + randint(min_lenght, max_lenght) * step
    return list(range(start, stop, step))


def progression_game():
    """Progression game."""
    rules = 'What number is missing in the progression?'
    rounds = []
    for _ in range(ROUNDS_AMOUNT):
        sequence = list(map(str, sequence_generator()))
        hided_index = choice(range(len(sequence)))
        right_answer = sequence[hided_index]
        sequence[hided_index] = '..'
        rounds.append((' '.join(sequence), right_answer))
    game(rules, rounds)


if __name__ == '__main__':
    progression_game()
