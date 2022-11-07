import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Kyle's Turtle Crossing Game (Use the 'Up' arrow to move)")


# initialize objects
player = Player()
car_manager = CarManager()
score = Scoreboard()

# move with up arrow key
screen.onkey(player.move, "Up")

# turn on game
game_is_on = True
while game_is_on:
    car_manager.spawn()
    car_manager.move_cars()
    time.sleep(0.05)
    screen.update()
    if player.ycor() == 290:
        score.increase_score()
        score.update_score()
        player.respawn()
        car_manager.speed_increase()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

# exit game by clicking screen
screen.exitonclick()
