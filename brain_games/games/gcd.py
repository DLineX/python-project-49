from random import randint


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def find_gcd(a: int, b: int):
    if a < b:
        a, b = b, a
    if a == 0 or b == 0:
        return a or b

    return find_gcd(b, a % b)


def show_rules():
    print('Find the greatest common divisor of given numbers.')


def get_round():
    UPPER_NUM = 100

    number1, number2 = randint(1, UPPER_NUM), randint(1, UPPER_NUM)

    question = ' '.join(map(str, (number1, number2)))
    gcd = find_gcd(number1, number2)

    return Round(question=question, answer=str(gcd))
