import random

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    answer = number1
    correct_answer = str(answer)
    return question, correct_answer
