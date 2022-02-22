import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
score = Scoreboard()



screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # car creating the cars
    car_manager.creat_car()
    car_manager.move_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # detect the sucess rate
    if player.finsh_line():
        player.go_start()
        car_manager.levelup()
        score.update()



screen.exitonclick()
