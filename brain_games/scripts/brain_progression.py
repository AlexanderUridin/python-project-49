#!/usr/bin/env python3


import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    if name != " ":
        print(f'Hello, {name}!')

def get_progression():
    first_num = random.randint(0, 10)
    progression = [first_num]
    len_of_progression = random.randint(5, 10)
    step = random.randint(1, 10)
    while len(progression) < len_of_progression:
        next_num = progression[-1] + step
        progression.append(next_num)
    return progression

def brain_progression():
    i = 0
    while i < 3:
        progression = get_progression()
        last_index = len(progression) -1
        random_index = random.randint(0, last_index)
        correct_answer = str(progression.pop(random_index))

        progression.insert(random_index, '..')
        question = ''
        for elem in progression:
            question += f'{elem} '

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        end = f"Let's try again, {name}!"
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer  ;(. Correct answer was {correct_answer} \n{end}")
            quit()       
        i += 1
    print(f'Congratulations, {name}!')
    quit()


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('What number is missing in the progression?')
    brain_progression()


if __name__ == '__main__':
    main()