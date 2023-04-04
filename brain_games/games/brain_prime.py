from random import randint
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(2, 100)
    question = (f'Question: {number}')
    true_answer = "yes" if is_prime_check(number) else "no"
    return question, true_answer


def is_prime_check(number):
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True
