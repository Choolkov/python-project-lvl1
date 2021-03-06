#!/usr/bin/env python
"""Script for brain-gcd game."""
from brain_games.engine import game_engine
from brain_games.games import gcd


def main():
    """Start brain-gcd game."""
    game_engine(gcd)


if __name__ == '__main__':
    main()
