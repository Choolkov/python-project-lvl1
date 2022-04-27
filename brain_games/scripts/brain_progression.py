#!/usr/bin/env python
"""Script for brain-progression game."""
from brain_games.engine import game_engine
from brain_games.games import progression


def main():
    """Start brain-progression game."""
    game_engine(progression)


if __name__ == '__main__':
    main()
