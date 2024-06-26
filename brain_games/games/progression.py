from random import randint


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def show_rules():
    print('What number is missing in the progression?')


def get_progression(item, step, lenght):
    progression = []
    for _ in range(lenght):
        progression.append(item)
        item += step
    return progression


def get_progression_with_hidden_item(progression: list, item_index: int)\
        -> str:
    hidden_item = [str(item) for item in progression]
    hidden_item[item_index] = '..'
    return ' '.join(hidden_item)


def get_round():
    UPPER_NUM = 100
    progression_item = randint(0, UPPER_NUM)

    LOWER_LENGHT, UPPER_LENGHT = 5, 15
    progression_lenght = randint(LOWER_LENGHT, UPPER_LENGHT)

    LOWER_STEP, UPPER_STEP = 1, 10
    progression_step = randint(LOWER_STEP, UPPER_STEP)

    progression = get_progression(
        progression_item, progression_step, progression_lenght)
    item_index = randint(0, progression_lenght - 1)

    question = get_progression_with_hidden_item(progression, item_index)
    hidden_num = progression[item_index]

    return Round(question=question, answer=str(hidden_num))
