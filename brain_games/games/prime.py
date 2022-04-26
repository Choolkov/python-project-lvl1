"""Prime game logic."""

from random import randint

from brain_games.engine import ROUNDS_AMOUNT, game


def isprime(number: int) -> bool:
    """
    Predicate for check positive integers for prime numbers.

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
