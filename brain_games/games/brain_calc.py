from random import randint, choice
import operator
RULES = 'What is the result of the expression?'


def get_calc():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    actions = ('*', '+', '-')
    action = choice(actions)
    operator = get_operator(action)
    true_answer = operator(first_number, second_number)
    question = f'Question: {first_number} {action} {second_number}'
    return question, str(true_answer)


def get_operator(action):
    if action == '+':
        return operator.add
    elif action == '-':
        return operator.sub
    else:
        return operator.mul


def get_question_and_answer():
    question, true_answer = get_calc()
    return question, true_answer
