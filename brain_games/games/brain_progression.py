from random import randint, choice
RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = build_progression()
    true_answer = choice(progression)
    index_element = progression.index(true_answer)
    progression[index_element] = '..'
    question = (f"Question: {' '.join(progression)}")
    return question, true_answer


def build_progression():
    first_number = randint(1, 50)
    step = randint(1, 10)
    progression_list = [str(first_number)]
    range_progression = 11
    for _ in range(range_progression):
        first_number += step
        progression_list.append(str(first_number))
    return progression_list
