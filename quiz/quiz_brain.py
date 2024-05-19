class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.scour = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False) : ")
        self.currect_answer(user_ans, current_question.answer)

    def currect_answer(self, user_answer, currect_answer):
        if user_answer.lower() == currect_answer.lower():
            self.scour += 1
            print("You got it Right!")
        else:
            print("That's wrong")
        print(f"The Currect answer is {currect_answer}")
        print(f"Your currect scour is {self.scour}/{self.question_number}")
        print("/n")
