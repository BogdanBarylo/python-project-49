#!/usr/bin/env python3
from math import gcd
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello

hello()
try_name = welcome_user()


def gsd():
    try_counter = 0
    max_try = 3
    print('Find the greatest common divisor of given numbers.')
    while try_counter < max_try:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        print(f'Question: {first_number} {second_number}')
        player_choice = input('Your answer: ')
        true_answer = gcd(first_number, second_number)
        if player_choice == str(true_answer):
            try_counter += 1
            print('Correct!')
        else:
            try_counter += 4
            print(f"{player_choice} is wrong answer ;(. Correct answer was {true_answer}. Let's try again, {try_name}!")
    if try_counter == max_try:
        print(f'Congurations, {try_name}!')


def main():
    gsd()


if __name__ == '__main__':
    main()
