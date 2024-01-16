import random

RULE = 'What is the result of the expression?'


def get_content():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    op = random.choice(operators)
    question = f'{number1} {op} {number2}'

    answer = 0

    if op == '+':
        answer = number1 + number2
    if op == '-':
        answer = number1 - number2
    if op == '*':
        answer = number1 * number2
    correct_answer = str(answer)

    return question, correct_answer
