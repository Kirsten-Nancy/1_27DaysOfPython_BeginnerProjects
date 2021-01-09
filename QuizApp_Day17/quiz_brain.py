class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question_index = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"{self.question_number}:"
                            f"{ current_question_index.question_text}(True/False)? ")
        # print(user_choice)
        self.check_answer(user_choice, current_question_index.answer)


    def more_questions_available(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("You are correct")
            self.score += 1
        else:
            print("Wrong answer.")
            print(f"The correct answer is {correct_answer}")

        print(f"Your current score is: {self.score}/{len(self.question_list)}")
        print()

