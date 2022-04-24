"""Even-game logic."""

from random import randint

from brain_games.games.engine import ROUNDS_AMOUNT, game


def even_game():
    """Even game."""
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    rounds = []
    for _ in range(ROUNDS_AMOUNT):
        number = randint(1, 100)
        right_answer = 'no' if number % 2 else 'yes'
        rounds.append((str(number), right_answer))
    game(rules, rounds)
