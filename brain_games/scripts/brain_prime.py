#!/usr/bin/env python3


import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    if name != " ":
        print(f'Hello, {name}!')
        

def brain_prime():
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        incorrect = f"'{answer}' is wrong answer ;(."
        end = f"Let's try again, {name}!"
        k = 0
        for z in range(2, number // 2+1):
            if (number % z == 0):
                k = k+1
        if (k <= 0):
            if answer == 'yes':
                print('Correct!')
            else:
                print(f"{incorrect} Correct answer was 'yes'. \n{end}")
                quit()
        else :
            if answer == 'yes':
                print(f"{incorrect} Correct answer was 'no'. \n{end}")
                quit()
            else:
                print('Correct!')
        i += 1
    print(f'Congratulations, {name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_prime()


if __name__ == '__main__':
    main()