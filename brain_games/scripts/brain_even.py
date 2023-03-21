#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello

hello()
try_name = welcome_user()


def even_check():
    try_counter = 0
    max_try = 3
    not_correct_1 = \
        "is wrong answer ;(. Correct answer was 'yes'. Let's try again,"
    not_correct_2 = \
        "is wrong answer ;(. Correct answer was 'no'. Let's try again,"
    print(f'Answer {"yes"} if the number is even, otherwise answer {"no"}')
    while try_counter < max_try:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        player_choise = input('Your answer: ')
        if random_number % 2 == 0 and player_choise == 'yes' or \
           random_number % 2 != 0 and player_choise == 'no':
            print('Correct!')
            try_counter += 1
        elif random_number % 2 == 0 and player_choise != 'yes':
            print(f"{player_choise} {not_correct_1} {try_name}!")
            try_counter += 4
        else:
            print(f"{player_choise} {not_correct_2} {try_name}!")
            try_counter += 4
    if try_counter == max_try:
        print(f'Congurations, {try_name}!')


def main():
    even_check()


if __name__ == '__main__':
    main()
