from math import sqrt


from random import randint


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def show_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def divides(a, b):
    return a % b == 0


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if divides(num, i):
            return False
    return True


def get_round():
    upper_num = 100
    number = randint(2, upper_num)
    answer = "yes" if is_prime(number) else "no"

    return Round(question=str(number), answer=answer)
