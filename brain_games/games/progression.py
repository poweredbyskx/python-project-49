from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(length, hidden_index):
    start = randint(1, 50)
    step = randint(1, 5)
    progression = [start + step * i for i in range(length)]
    progression[hidden_index] = '..'
    return progression, start, step


def generate_game():
    progression_length = randint(5, 10)
    hidden_index = randint(0, progression_length - 1)

    progression, start, step = generate_progression(progression_length, hidden_index) # NOQA

    expression = ' '.join(map(str, progression))
    correct_answer = str(start + step * hidden_index)
    return expression, correct_answer
