from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_game():
    random_num = randint(1, 100)
    question = str(random_num)
    correct_answer = 'yes' if is_even(random_num) else 'no'
    return random_num, correct_answer
