import prompt


def game_engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = game.generate_game()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # NOQA
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")
