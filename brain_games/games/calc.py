from random import randint, choice


from operator import add, sub, mul


from typing import NamedTuple


Round = NamedTuple('Round', [('question', str), ('answer', str)])


def show_rules():
    print('What the result of the exprassion?')


def get_round():
    upper_num = 100

    operations = {'+': add, '-': sub, '*': mul}
    number1, number2 = randint(1, upper_num), randint(1, upper_num)
    operation_symbol = choice(tuple(operations.keys()))

    question = ' '.join(map(str, (number1, operation_symbol, number2)))
    result = operations[operation_symbol](number1, number2)

    return Round(question=question, answer=str(result))
