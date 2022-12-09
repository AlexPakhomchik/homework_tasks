import random


class Mystery:
    def __init__(self, question: str, answer, choices: list):
        self.question = question
        self.answer = answer
        self.choices = choices

    difficult = 0
    sum_marks = 0

    @staticmethod
    def append_answer_in_choices(answer, choices):
        choices.append(answer)

    @staticmethod
    def mix_choices(choices):
        return random.shuffle(choices)

    @staticmethod
    def choices_print(choices):
        for i in range(len(choices)):
            print(f'{" " * 10}{i}. {choices[i]}')

    @staticmethod
    def question_print(question):
        print(f'Question: {question}')

    def sum(self, bool):
        x = 3 if bool else -3
        self.sum_marks += x

    def processing_choice(self, answer, choices, sum_marks):
        y = int(input('Select option '))
        x = answer == choices[y]
        self.sum(x)
        print(x)

    def quiz(self):
        self.question_print(self.question)
        self.append_answer_in_choices(self.answer, self.choices)
        self.mix_choices(self.choices)
        self.choices_print(self.choices)
        self.processing_choice(self.answer, self.choices, self.sum_marks)


q1 = Mystery(question="2 + 2 = ? ",
             answer="4",
             choices=[
                 "2",
                 "1",
                 "5",
                 "3"
             ])


