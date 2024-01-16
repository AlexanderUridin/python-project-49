import random

RULE = 'What number is missing in the progression?'


def get_progression():
    first_num = random.randint(0, 10)
    progression = [first_num]
    len_of_progression = random.randint(5, 10)
    step = random.randint(1, 10)
    while len(progression) < len_of_progression:
        next_num = progression[-1] + step
        progression.append(next_num)
    return progression


def get_content():
    progression = get_progression()
    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)
    correct_answer = str(progression.pop(random_index))

    progression.insert(random_index, '..')
    question = ''
    for elem in progression:
        question += f'{elem} '
    return question, correct_answer
