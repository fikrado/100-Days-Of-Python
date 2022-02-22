from turtle import *


# screen ---------------------------------------------------
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)


# Right paddle-------------------------------------------------
right_pad = Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# left pandel-------------------------------------------
left_pad = Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# right move-----------------------------------------------
def R_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
def R_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# left move-----------------------------------------------
def L_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
def L_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

# move ment ----------------------------------------------
screen.listen()
screen.onkey(R_up, "Up")
screen.onkey(R_down, "Down")
screen.onkey(L_up, "w")
screen.onkey(L_down, "s")

# Now, we will initialize the score ---------------------------
left_player = 0
right_player = 0

# score screeen  ---------------------------------------------
sketch_1 = Turtle()
sketch_1.speed(0)
sketch_1.color("blue")
sketch_1.penup()
sketch_1.hideturtle()
sketch_1.goto(0, 260)
sketch_1.write("Left Player : 0    Right Player: 0", align="center", font=("Courier", 24, "normal"))


# boll --------------------------------------------------------
hit_ball = Turtle()
hit_ball.color("white")
hit_ball.shape("circle")
hit_ball.speed(0)
hit_ball.penup()
hit_ball.dx = 5
hit_ball.dy = -5

# game one ----------------------------------------------------
game_on =True
while game_on:
    screen.update()
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Check all the borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch_1.clear()
        sketch_1.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch_1.clear()
        sketch_1.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",font=("Courier", 24, "normal"))

        # Collision of ball and paddles
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() - 40):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1


# it while exte on click -------------------------------------
screen.exitonclick()
