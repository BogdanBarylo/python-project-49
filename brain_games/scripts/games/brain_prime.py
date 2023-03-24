#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello

hello()
try_name = welcome_user()


def prime():
    try_counter = 0
    max_try = 3
    dict_answers = {'yes': 'no',
                    'no': 'yes'}
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while try_counter < max_try:
        number = randint(2, 100)
        print(f'Question: {number}')
        player_choice = input('Your answer: ')
        count = 1
        primes_count = 0
        while count <= number:
            if number % count == 0:
                primes_count += 1
            count += 1
        if primes_count == 2 and player_choice == 'yes' or \
           primes_count != 2 and player_choice == 'no':
            try_counter += 1
            print('Correct!')
        else:
            print(f"'{player_choice}' is wrong answer ;(. "
                  f"Correct answer was '{dict_answers.get(player_choice)}'. "
                  f"Let's try again, {try_name}!")
            try_counter += 4
    if try_counter == max_try:
        print(f'Congratulations, {try_name}!')


def main():
    prime()


if __name__ == '__main__':
    main()
