import prompt
MAX_ROUNDS = 3


def run(RULES, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(RULES)
    counter_true_answers = 0
    for _ in range(MAX_ROUNDS):
        question, answer = get_question_and_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. "
                  f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            counter_true_answers += 1
    if counter_true_answers == MAX_ROUNDS:
        print(f'Congratulations, {name}!')
