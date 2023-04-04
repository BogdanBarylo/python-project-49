from math import gcd
from random import randint
RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'Question: {first_number} {second_number}'
    true_answer = gcd(first_number, second_number)
    return question, str(true_answer)
