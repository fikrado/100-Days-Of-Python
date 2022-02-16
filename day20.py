from turtle import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PYTHON   SNAKE   GAME")

t = Turtle()
starting = [(0, 0), (-20, 0), (-40, 0)]

for sq in starting:
    t.shape("square")
    t.color("white")
    t.goto(sq)






screen.exitonclick()