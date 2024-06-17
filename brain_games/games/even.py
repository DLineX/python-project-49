from random import randint


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number: int):
    return number % 2 == 0


def get_round():
    upper_num = 100

    number = randint(0, upper_num)
    answer = "yes" if is_even(number) else "no"
    return Round(question=number, answer=answer)
