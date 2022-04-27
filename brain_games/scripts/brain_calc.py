#!/usr/bin/env python
"""Script for brain-calc game."""
from brain_games.engine import game_engine
from brain_games.games import calc


def main():
    """Start brain-calc game."""
    game_engine(calc)


if __name__ == '__main__':
    main()
