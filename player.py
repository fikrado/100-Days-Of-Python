from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.go_start()
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def go_start(self):
        self.goto(STARTING_POSITION)

    def finsh_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
