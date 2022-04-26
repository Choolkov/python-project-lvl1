"""Calc-game logic."""

from operator import add, mul, sub
from random import choice, randint

from brain_games.engine import ROUNDS_AMOUNT, game

min_number = 1
max_number = 50


def calc(expression: str) -> str:
    """
    Calculate math expressions of two values with plus minus or asterisk signs.

    Return string of result.

    Args:
        expression: math expression

    Returns:
        str

    """
    math_signs = {'+': add, '-': sub, '*': mul}
    value1, sign, value2 = expression.split()
    return str(math_signs[sign](int(value1), int(value2)))


def calc_game():
    """Calc game."""
    rules = 'What is the result of the expression?.'
    rounds = []
    for _ in range(ROUNDS_AMOUNT):
        number1 = str(randint(1, max_number))
        number2 = str(randint(1, max_number))
        expression = ' '.join((number1, choice('+-*'), number2))
        rounds.append((expression, calc(expression)))
    game(rules, rounds)


if __name__ == '__main__':
    calc_game()
