from random import randint
from brain_games.cli import welcome_user

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print('What number is missing in the progression?')

    score = 0
    while score < 3:
        def generate_progression(length, hidden_index):
            start = randint(1, 50)
            step = randint(1, 5)
            progression = [start + step * i for i in range(length)]
            progression[hidden_index] = '..'
            return progression

        def generate_game():
            progression_length = randint(5, 10)
            hidden_index = randint(0, progression_length - 1)
            progression = generate_progression(progression_length, hidden_index)

            correct_answer = str(progression[hidden_index - 1] + (progression[hidden_index - 1] - progression[hidden_index - 2]))

            return progression, correct_answer

        progression, correct_answer = generate_game()
        progression_str = " ".join(map(str, progression))

        print(f'Question: {progression_str}')

        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            score = 0
            break

    if score == 3:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()

