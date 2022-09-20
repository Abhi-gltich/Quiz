from data import question_data
from question_model import Question
from quiz_brain import Brains

question_bank = []

for x in range(len(question_data)):
    dataset = question_data[x]
    text = dataset["question"]
    answer = dataset["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = Brains(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your total score is {quiz.score}/{len(question_bank)}")
