#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello

hello()
try_name = welcome_user()


def even_check():
    try_counter = 0
    max_try = 3
    dict_answers = {'yes': 'no',
                    'no': 'yes'}
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while try_counter < max_try:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        player_choice = input('Your answer: ')
        if random_number % 2 == 0 and player_choice == 'yes' or \
           random_number % 2 != 0 and player_choice == 'no':
            print('Correct!')
            try_counter += 1
        else:
            print(f"'{player_choice}' is wrong answer ;(. "
                  f"Correct answer was '{dict_answers.get(player_choice)}'. "
                  f"Let's try again, {try_name}!")
            try_counter += 4
    if try_counter == max_try:
        print(f'Congratulations, {try_name}!')


def main():
    even_check()


if __name__ == '__main__':
    main()
