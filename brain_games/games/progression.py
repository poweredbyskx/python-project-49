from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(length, hidden_index):
    start = randint(1, 50)
    step = randint(1, 10)
    progression = [start + step * i for i in range(length)]
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    return progression, correct_answer


def generate_game():
    progression_length = randint(5, 10)
    hidden_index = randint(0, progression_length - 1)
    progression, correct_answer = generate_progression(progression_length, hidden_index)
    question = " ".join(progression)
    return question, correct_answer
