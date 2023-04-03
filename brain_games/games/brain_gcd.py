from math import gcd
from random import randint
RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'Question: {first_number} {second_number}'
    true_answer = find_gcd(first_number, second_number)
    return question, str(true_answer)


def find_gcd(first_number, second_number):
    return gcd(first_number, second_number)


def get_question_and_answer():
    question, true_answer = get_gcd()
    return question, true_answer
