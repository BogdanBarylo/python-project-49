#!/usr/bin/env python3
from brain_games.cli import ask_name


def say_hello():
    print('Welcome to the Brain Games!')


def main():
    say_hello()
    ask_name()


if __name__ == '__main__':
    main()
