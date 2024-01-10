#!/usr/bin/env python3


import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    if name != " ":
        print(f'Hello, {name}!')


def brain_even():
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operators = [ '+' , '-' , '*' ]
        op = random.choice(operators)
        result = f'{number1} {op} {number2}'
        print(f'Question: {result}')
        answer = prompt.integer('Your answer: ')
        end = f"Let's try again, {name}!"
        if op == '+':
            result = number1 + number2
            if answer == result:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer  ;(. Correct answer was {result} \n{end}")
                quit()
        if op == '-':
            result = number1 - number2
            if answer == result:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer  ;(. Correct answer was {result} \n{end}")
                quit()
        if op == '*':
            result = number1 * number2
            if answer == result:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer  ;(. Correct answer was {result} \n{end}")
                quit()        
        i += 1
    print(f'Congratulations, {name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('What is the result of the expression?')
    brain_even()


if __name__ == '__main__':
    main()