class QuizzBrain():
    def __init__(self, ques_list):
        self.ques_no = 0
        self.ques_list = ques_list
        self.score = 0

    def next_ques(self):
        current_ques = self.ques_list[self.ques_no]
        self.ques_no += 1
        user_ans = input(f"Q.{self.ques_no}: {current_ques.text} (True / False)?\n")
        self.check_ans(user_ans, current_ques.answer)

    def still_has_ques(self):
        if self.ques_no < len(self.ques_list):
            return True
        else:
            return False

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.ques_no}")
        print("\n")

