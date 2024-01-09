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
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        incorrect = f"'{answer}' is wrong answer ;(."
        end = f"Let's try again, {name}!"
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print(f"{incorrect} Correct answer was 'yes'. \n{end}")
                quit()
        if number % 2 != 0:
            if answer == 'no':
                print('Correct!')
            else:
                print(f"{incorrect} Correct answer was 'no'. \n{end}")
                quit()
        i += 1
    print(f'Congratulations, {name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even()


if __name__ == '__main__':
    main()
