from random import randint
from brain_games.cli import welcome_user

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')

    def simple_num(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    score = 0
    while score < 3:
        number = randint(1, 100)
        print(f'Question: {number}')

        result = "yes" if simple_num(number) else "no"
        user = input("Your answer: ")

        if user == result:
            print('Correct!')
            score += 1
        else:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            score = 0
            break

    if score == 3:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()

