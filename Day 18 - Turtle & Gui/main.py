import turtle
from turtle import Turtle, Screen
import random

# initialize
turtle.colormode(255)  # allows us to use 0-255 for rgb values
tim = Turtle()
screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


# attributes
tim.shape("turtle")
tim.color("red")


colors = ["mint cream", "pale turquoise", "navy", "dodger blue", "yellow", "maroon", "violet red"]
headings = [0, 90, 180, 270]

# spirograph!
tim.speed(0)
number_of_turns = 72
for _ in range(number_of_turns):
    tim.color(random_color())
    tim.circle(100)
    tim.right(360/number_of_turns)



# # random walk
# tim.pensize(3)
# tim.speed(10)
# for _ in range (300):
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(headings))
#     tim.forward(30)


# number_of_sides = 2
# while number_of_sides < 8:
#     number_of_sides += 1
#     angle = 360/number_of_sides
#     tim.color(random.choice(colors))
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)


# # drawing a dotted line
# def draw_10_move_20(turtle_object):
#     turtle_object.forward(10)
#     turtle_object.penup()
#     turtle_object.forward(10)
#     turtle_object.pendown()
#
#
# for _ in range(50):
#     draw_10_move_20(tim)


# drawing a square
# square_distance = 100
# tim.forward(square_distance)
# tim.left(90)
# tim.forward(square_distance)
# tim.left(90)
# tim.forward(square_distance)
# tim.left(90)
# tim.forward(square_distance)
# tim.left(90)

screen.exitonclick()
