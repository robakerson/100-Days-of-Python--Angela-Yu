from turtle import Turtle, Screen
from random import randint

#  initialize turtle & screen
screen = Screen()
screen.setup(500, 400)  # setup screen to 500w 400h
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle("turtle")
tom = Turtle("turtle")
terry = Turtle("turtle")
tyler = Turtle("turtle")
theo = Turtle("turtle")
dave_grohl = Turtle("turtle")
turtles = [tim, tom, terry, tyler, theo, dave_grohl]


def turtle_setup(turtle, color, yposition):  # turtle_setup makes new turtle with chosen parameters
    turtle.color(color)
    turtle.up()
    turtle.setpos(-230, yposition)


yposition = -75
for num in range(6):  # set up 6 turtles
    turtle_setup(turtles[num], colors[num], yposition)
    yposition += 30


# ensure user input is good before running race
is_race_on = False
if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:  # winning condition
            winner = turtle  # current turtle is the winner
            if winner.pencolor() == user_bet:
                print(f"You win! The winning color is {winner.pencolor()}.")
            else:
                print(f"You lost! The winning color is {winner.pencolor()}.")
            is_race_on = False  # stop the race!

# print(f"Winner is {winner.pencolor()}")

# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_left():
#     tim.left(10)
#
#
# def move_right():
#     tim.right(10)
#
#
# def clear_drawing():
#     tim.setheading(0)
#     tim.setpos(0,0)
#     tim.clear()
#
#
# screen.listen()
# tim.speed(3)
# screen.onkey(move_forwards, "w")  # onkey will call the function when space is pressed
# screen.onkey(move_backwards, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear_drawing, "c")

screen.exitonclick()