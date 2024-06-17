import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
