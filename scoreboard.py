from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.leve = 1
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.write(f"level: {self.leve} ", align="left", font=FONT)

    def update(self):
        self.leve += 1
        self.clear()
        self.write(f"level: {self.leve} ", align="left", font=FONT)


