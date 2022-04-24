"""Prime game logic."""

from random import randint

from brain_games.games.engine import ROUNDS_AMOUNT, game
from sympy import isprime


def prime_game():
    """Prime game."""
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    rounds = []
    max_number = 50
    for _ in range(ROUNDS_AMOUNT):
        number = randint(1, max_number)
        right_answer = 'yes' if isprime(number) else 'no'
        rounds.append((str(number), right_answer))
    game(rules, rounds)


if __name__ == '__main__':
    prime_game()
