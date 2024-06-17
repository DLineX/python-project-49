from random import randint


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def find_gcd(a, b) -> int:
    if a > b:
        a, b = b, a
    if a == 0 or b == 0:
        return a or b
    return find_gcd(b, a % b)


def show_rules():
    print('Find the greatest common divisor of given numbers')


def get_round():
    upper_num = 100

    number1, number2 = randint(1, upper_num), randint(1, upper_num)

    question = ''.join(map(str, (number1, number2)))
    gcd = find_gcd(number1, number2)
    return Round(question=question, answer=str(gcd))
