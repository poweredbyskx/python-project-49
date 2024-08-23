from random import randint
from brain_games.cli import welcome_user

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print(f'Hello, {name}!')
    print(f'What number is missing in the progression?')

    score = 0
    while score < 3:
        def generate_progression(length, hidden_index):
            start = randint(1, 50)
            step = randint(1, 5)
            progression = [start + step * i for i in range(length)]
            progression[hidden_index] = '..'
            return progression, start, step

        def generate_game():
            progression_length = randint(5, 10)
            hidden_index = randint(0, progression_length - 1)
            progression, start, step = generate_progression(progression_length, hidden_index)

            correct_answer = str(start + step * hidden_index)

            return progression, correct_answer
        progression, correct_answer = generate_game()

        print(f'Question: {progression}')

        user = correct_answer
        user = input("Your answer: ")

        if user == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            score = 0
            break

    if score == 3:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()
