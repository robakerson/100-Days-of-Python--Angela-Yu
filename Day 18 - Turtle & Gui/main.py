from turtle import Turtle, Screen
import random

# initialize
tim = Turtle()
screen = Screen()

# attributes
tim.shape("turtle")
tim.color("red")


colors = ["mint cream", "pale turquoise", "navy", "dodger blue", "yellow", "maroon", "violet red"]
number_of_sides = 2
while number_of_sides < 8:
    number_of_sides += 1
    angle = 360/number_of_sides
    tim.color(random.choice(colors))
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


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
