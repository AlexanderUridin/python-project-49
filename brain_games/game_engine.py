import prompt

ROUNDS_COUNT = 3


def launch_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.GAME_RULE)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_game()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    else:
        print(f'Congratulations, {name}!')
