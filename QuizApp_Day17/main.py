from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    # Creating a bank of Question objects
    question_bank.append(Question(data['question'], data['correct_answer']))

# print(question_bank[0].answer)
quiz_brain = QuizBrain(question_bank)
while quiz_brain.more_questions_available():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}")