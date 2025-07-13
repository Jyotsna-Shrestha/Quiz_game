class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def remaining_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        ans = input(f'Q.{self.question_number + 1}. {question.text} (True/False)?: ')
        if ans.title() == question.answer:
            self.score += 1
            print('Correct!')
        else:
            print('Incorrect.')
        self.question_number += 1
        print(f'Your score is {self.score}/{len(self.question_list)}')