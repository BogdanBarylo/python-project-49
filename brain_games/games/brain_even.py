#!/usr/bin/env python3
from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_check():
    random_number = randint(1, 100)
    question = f'Question: {str(random_number)}'
    true_answer = "yes" if is_even(random_number) else "no"
    return question, true_answer


def is_even(random_number):
    if random_number % 2 == 0:
        return True
    else:
        return False


def get_question_and_answer():
    question, true_answer = even_check()
    return question, true_answer
