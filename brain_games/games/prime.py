import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_content():
    number = random.randint(1, 100)
    question = number
    k = 0
    for z in range(2, number // 2 + 1):
        if (number % z == 0):
            k = k + 1
    if (k <= 0):
        answer = 'yes'
    else:
        answer = 'no'
    correct_answer = str(answer)
    return question, correct_answer
