from question_model import Question
from data import  question_data
from quiz_brain import QuizzBrain

question_bank = []
for x in question_data:
    ques_text = x["question"]
    ques_answer = x["correct_answer"]
    ques = Question(ques_text, ques_answer)
    question_bank.append(ques)

quiz = QuizzBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_ques()

print("You have completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.ques_no}")

