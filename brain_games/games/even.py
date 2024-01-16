import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_content():
    question = random.randint(1, 100)
    number = question
    answer = ''
    if number % 2 == 0:
        answer = 'yes'
    if number % 2 != 0:
        answer = 'no'
    correct_answer = str(answer)
    return question, correct_answer
