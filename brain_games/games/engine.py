"""Common game logic."""

import prompt

ROUNDS_AMOUNT = 3   # количество раундов


def get_useraname() -> str:
    """
    Welcome user and return username.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def game(rules: str, rounds: tuple):
    """
    Game engine.

    Args:
        rules: game rules
        rounds: list of tuples (question, right answer)
    """
    name = get_useraname()
    print(rules)
    for question, right_answer in rounds:
        print('Question: {0}'.format(question))
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
