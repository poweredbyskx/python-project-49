from random import randint, choice
from brain_games.cli import welcome_user

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print(f'What is the result of the expression?')

    score = 0
    while score < 3:
        random_num1 = randint(1, 100)
        symbol = choice(['+', '-', '*'])
        random_num2 = randint(1, 100)

        print(f'Question: {random_num1} {symbol} {random_num2}')

        user_answer = int(input("Your answer: "))

        if symbol == '+':
            result = random_num1 + random_num2
        elif symbol == '-':
            result = random_num1 - random_num2
        elif symbol == '*':
            result = random_num1 * random_num2

        if user_answer == result:
            print('Correct!')
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            score = 0
            break

    if score == 3:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()

