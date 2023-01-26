class QuizBrain:
    def __init__(self, list):
        self.question_no = 0
        self.question_list = list
        self.score = 0
    
    def still_have_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        question = input(f" Q{self.question_no}: {current_question.text} (True / False) ").title()
        if question == current_question.answer:
            print("Correct, You made the right choice")
            print(f"The correct answer is: {current_question.answer}")
            self.score += 1
            print(f"Your current score is {self.score} / {self.question_no}")
            
        elif question != current_question.answer:
            print("Incorrect, You made the wrong choice")
            print(f"The correct answer is: {current_question.answer}")
            print(f"Your current score is {self.score} / {self.question_no}") 
             

    def final_score(self):
        print('You have completed the quiz')
        print(f"Your final score is {self.score} / {self.question_no} ")

