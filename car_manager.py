from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2
X_SPAWN = 300
Y_SPAWN = range(-300, 300, 10)


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_distance = 2

    def spawn(self):
        rand_int = randint(1, 20)
        if rand_int == 6:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(X_SPAWN, choice(Y_SPAWN))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(self.move_distance)

    def speed_increase(self):
        self.move_distance += 2
