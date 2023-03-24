#!/usr/bin/env python3
from random import randint, choice
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello

hello()
try_name = welcome_user()


def calc():
    try_counter = 0
    max_try = 3
    print('What is the result of the expression?')
    while try_counter < max_try:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        actions = ('*', '+', '-')
        action = choice(actions)
        print(f'Question: {first_number} {action} {second_number}')
        if action == '+':
            true_answer = first_number + second_number
        elif action == '-':
            true_answer = first_number - second_number
        else:
            true_answer = first_number * second_number
        player_choice = input('Your answer: ')
        if player_choice == str(true_answer):
            try_counter += 1
            print('Correct!')
        else:
            try_counter += 4
            print(f"'{player_choice}' is wrong answer ;(. "
                  f"Correct answer was {true_answer}. "
                  f"Let's try again, {try_name}!")
    if try_counter == max_try:
        print(f'Congurations, {try_name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
