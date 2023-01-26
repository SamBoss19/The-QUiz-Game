from Questionformat import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    p_question = questions['text']
    p_answer = questions['answer']
    real_question = Question(p_question, p_answer)
    question_bank.append(real_question)

quiz = QuizBrain(question_bank)
while quiz.still_have_questions() == True:
    quiz.next_question()
else:
    quiz.final_score()
