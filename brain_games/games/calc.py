from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice(['+', '-', '*'])

    question = f"{number1} {operator} {number2}"

    if operator == '+':
        correct_answer = str(number1 + number2)
    elif operator == '-':
        correct_answer = str(number1 - number2)
    elif operator == '*':
        correct_answer = str(number1 * number2)

    return question, correct_answer
