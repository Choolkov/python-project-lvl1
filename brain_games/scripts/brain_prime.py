#!/usr/bin/env python
"""Script for brain-prime game."""
from brain_games.engine import game_engine
from brain_games.games import prime


def main():
    """Start brain-prime game."""
    game_engine(prime)


if __name__ == '__main__':
    main()
