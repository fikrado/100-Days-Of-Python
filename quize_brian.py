class QuizBrain:
    def __init__(self, qlist):
        self.qnuber = 0
        self.score = 0
        self.list = qlist

    def still_has_qustions(self):
        return self.qnuber < len(self.list)


    def retrieve(self):
        curent_qustion = self.list[self.qnuber]
        self.qnuber +=  1
        user_answer = input(f" Q = {self.qnuber} : {curent_qustion.text}  is it TRUE OR FLASE")
        self.check_answer(user_answer, curent_qustion.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("correct answer")
        else:
            print("wrong asnwer please try again later ")

        print(f"the correct answer was {correct_answer} and \nyour socore is {self.score} / {self.qnuber}")
        print("\n")


