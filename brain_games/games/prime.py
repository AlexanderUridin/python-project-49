import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    for z in range(2, number // 2 + 1):
        if (number % z == 0):
            k = k + 1
    if (k <= 0):
        return False
    else:
        return True


def get_game():
    number = random.randint(1, 100)
    question = number
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    return question, correct_answer
