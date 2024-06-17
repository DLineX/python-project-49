#!/usr/bin/env python3
from brain_games.games import calc as calc_game


from brain_games.engine import play


def main():
    play(calc_game)


if __name__ == '__main__':
    main()
