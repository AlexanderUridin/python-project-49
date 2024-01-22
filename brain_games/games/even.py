import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    if number % 2 != 0:
        return False


def get_game():
    question = random.randint(1, 100)
    number = question
    correct_answer = 'yes' if is_even(number) is True else 'no'
    return question, correct_answer
