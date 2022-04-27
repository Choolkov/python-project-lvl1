#!/usr/bin/env python
"""Script for brain-even game."""
from brain_games.engine import game_engine
from brain_games.games import even


def main():
    """Start brain-even game."""
    game_engine(even)


if __name__ == '__main__':
    main()
