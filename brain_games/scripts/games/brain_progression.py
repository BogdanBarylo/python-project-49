#!/usr/bin/env python3
from random import randint, choice
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello

hello()
try_name = welcome_user()


def progression():
    try_counter = 0
    max_try = 3
    print('What number is missing in the progression?')
    while try_counter < max_try:
        count = 0
        first_number = randint(1, 50)
        step = randint(1, 10)
        list_progression = [str(first_number)]
        while count != 10:
            first_number += step
            list_progression.append(str(first_number))
            count += 1
        true_answer = choice(list_progression)
        index_element = list_progression.index(true_answer)
        list_progression[index_element] = '..'
        print(f"Question: {' '.join(list_progression)}")
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
        print(f'Congratulations, {try_name}!')


def main():
    progression()


if __name__ == '__main__':
    main()
