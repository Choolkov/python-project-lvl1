"""Client functions."""

import prompt


def welcome_user():
    """User welcome function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
