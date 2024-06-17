from types import ModuleType


import prompt


from brain_games.cli import welcome


def play(game: ModuleType):
    welcome()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    game.show_rules()
    for _ in range(3):
        round = game.get_round()
        print(f'Question: {round.question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != round.answer:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f"Correct answer is '{round.answer}'.")
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
