#!/usr/bin/env python
"""Script for brain-games."""
from brain_games.cli import welcome_user


def main():
    """Show welcome message and greeting user."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
