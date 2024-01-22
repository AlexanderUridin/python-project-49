#!/usr/bin/env python3

from brain_games.game_engine import launch_game
from brain_games.games import even


def main():
    launch_game(even)


if __name__ == '__main__':
    main()
