from random import randint, choice


from operator import add, sub, mul


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def show_rules():
    print('What is the result of the expression?')


def get_round():
    UPPER_NUM = 100

    OPERATIONS = {'+': add, '-': sub, '*': mul}
    number1, number2 = randint(1, UPPER_NUM), randint(1, UPPER_NUM)
    operation_symbol = choice(tuple(OPERATIONS.keys()))

    question = ' '.join(map(str, (number1, operation_symbol, number2)))
    result = OPERATIONS[operation_symbol](number1, number2)

    return Round(question=question, answer=str(result))
