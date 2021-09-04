import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("FROGGER!")

player = Player()
screen.listen()
screen.onkeypress(fun=player.move_player, key="Up")

scoreboard = Scoreboard()

cars = CarManager()
player_level = 0
game_is_on = True
new_car = 0
while game_is_on:
    if player.check_finish_line():
        player.reset_player()
        player_level += 1
        scoreboard.increase_level()
    cars.move_cars(player_level)
    time.sleep(0.1)
    screen.update()
    cars.new_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


screen.exitonclick()