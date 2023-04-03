from random import randint
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_prime_check():
    number = randint(2, 100)
    question = (f'Question: {number}')
    true_answer = "yes" if is_prime_check(number) else "no"
    return question, true_answer


def is_prime_check(number):
    count = 1
    primes_count = 0
    while count <= number:
        if number % count == 0:
            primes_count += 1
        count += 1
    if primes_count == 2:
        return True
    else:
        return False


def get_question_and_answer():
    question, true_answer = get_prime_check()
    return question, true_answer
