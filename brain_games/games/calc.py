import random

GAME_RULE = 'What is the result of the expression?'


def calculate_expression(number1, number2, op):
    if op == '+':
        answer = number1 + number2
    if op == '-':
        answer = number1 - number2
    if op == '*':
        answer = number1 * number2
    return answer


def get_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    op = random.choice(operators)
    question = f'{number1} {op} {number2}'

    correct_answer = str(calculate_expression(number1, number2, op))

    return question, correct_answer
