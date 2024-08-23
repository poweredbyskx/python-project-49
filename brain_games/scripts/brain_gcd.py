from random import randint
from brain_games.cli import welcome_user

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()

    print(f'Find the greatest common divisor of given numbers.')

    score = 0
    while score < 3:
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 100)

        print(f'Question: {random_num1} {random_num2}')

        user = int(input("Your answer: "))

        while random_num1 != 0 and random_num2 != 0:

            if random_num1 > random_num2:
                random_num1 %= random_num2
            else:
                random_num2 %= random_num1
        result = random_num1 + random_num2

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
