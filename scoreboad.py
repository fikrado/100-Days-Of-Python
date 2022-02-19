from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.write(f"score: {self.score}", align='center', font=('Arial', 25, 'normal'))
        self.hideturtle()


    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align='center', font=('Arial', 25, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER (-_-)a\n score = {self.score}", align='center', font=('Arial', 25, 'normal'))
