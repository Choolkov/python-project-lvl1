"""Even-game logic."""

from random import randint

import prompt


def even_game():
    """Even game."""
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 100)
        right_answer = 'no' if number % 2 else 'yes'
        print('Question: {0}'.format(number))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer \
was '{1}'.".format(user_answer, right_answer),
            )
            print("Let's try again, {0}!".format(name))
            return
    print('Congratulations, {0}!'.format(name))
