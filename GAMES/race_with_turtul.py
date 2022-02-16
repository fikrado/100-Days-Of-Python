from turtle import *
from random import *

colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
race_on = True
screen = Screen()
screen.setup(width=500, height=400)
y_posrions = [-70, -40, -10, 20, 50, 80]
all_t = []
ubet = screen.textinput(title="make a pit", prompt="which tutle will win")

for tur in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.speed("fastest")
    t.color(colors[tur])
    t.goto(x=-230, y=y_posrions[tur])
    all_t.append(t)

if ubet:
    race_on = True
while race_on:
    for turtle in all_t:
        if turtle.xcor() > 230:
            race_on = False
            wcolor = turtle.pencolor()
            if wcolor == ubet:
                print(f"you wine with {wcolor} turtle")
            else:
                print(f"sorry loser the winer is {wcolor} turtle")
        distan = randint(0, 10)
        turtle.forward(distan)

screen.bgcolor("black")
screen.exitonclick()
