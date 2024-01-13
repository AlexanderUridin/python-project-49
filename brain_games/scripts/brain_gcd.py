#!/usr/bin/env python3


import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    if name != " ":
        print(f'Hello, {name}!')


def brain_gcd():
    i = 0
    while i < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f'Question: {number1} {number2}')
        answer = prompt.integer('Your answer: ')
        end = f"Let's try again, {name}!"
        while number1 != number2:
            if number1 > number2:
                number1 = number1 - number2
            else:
                number2 = number2 - number1
        if answer == number1:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer  ;(. Correct answer was {number1} \n{end}")
            quit()        
        i += 1
    print(f'Congratulations, {name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('What is the result of the expression?')
    brain_gcd()


if __name__ == '__main__':
    main()