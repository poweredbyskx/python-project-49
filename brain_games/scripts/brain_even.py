from random import randint
from brain_games.cli import welcome_user

def even_num(number):
    return number % 2 == 0

def even_num_game(name):
    print(f'Answer "yes" if the number is even, otherwise answer "no".')

    score = 0
    while score < 3:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')

        user = input("Your answer: ")

        if even_num(random_num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

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

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    even_num_game(name)

if __name__ == "__main__":
    main()

