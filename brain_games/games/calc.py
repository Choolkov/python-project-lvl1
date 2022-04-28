"""Calc-game logic."""

from operator import add, mul, sub
from random import choice, randint

MAX_NUMBER = 10
RULES = 'What is the result of the expression?.'


def calc(expression: str) -> str:
    """
    Calculate math expressions of two numbers with plus minus or asterisk signs.

    Return string of result.

    Args:
        expression: math expression

    Returns:
        str

    """
    math_signs = {'+': add, '-': sub, '*': mul}
    value1, sign, value2 = expression.split()
    return str(math_signs[sign](int(value1), int(value2)))


def get_round() -> tuple:
    """
    Return round for calc-game.

    Returns:
        tuple: question and right answer
    """
    number1 = str(randint(1, MAX_NUMBER))
    number2 = str(randint(1, MAX_NUMBER))
    expression = ' '.join((number1, choice('+-*'), number2))
    return expression, calc(expression)
