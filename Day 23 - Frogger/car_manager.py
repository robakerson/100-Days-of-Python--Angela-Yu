from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def new_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.up()
            new_car.color(choice(COLORS))
            y_cor = randint(-250, 250)
            new_car.setpos(300, y_cor)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self, player_level):
        for car in self.all_cars:
            new_x_cor = car.xcor() - STARTING_MOVE_DISTANCE - (MOVE_INCREMENT * player_level - 1)
            car.setpos(new_x_cor, car.ycor())
            if car.xcor() < -320:
                self.all_cars.remove(car)

