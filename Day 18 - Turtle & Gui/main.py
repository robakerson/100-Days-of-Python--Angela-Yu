import turtle
from turtle import Turtle, Screen
import random
import colorgram # needed to extract colors from jpeg

# initialize
turtle.colormode(255)  # allows us to use 0-255 for rgb values
tim = Turtle()
screen = Screen()
tim.penup()

# #  extract colors from .jpg
# colors = colorgram.extract('painting2.jpg', 30)
# list_of_colors = []
# for value in colors:
#     r = value.rgb.r
#     g = value.rgb.g
#     b = value.rgb.b
#     list_of_colors.append((r,g,b))
# print(list_of_colors)

list_of_colors = [(26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72), (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162), (30, 91, 95), (87, 47, 34), (34, 46, 84)]

y_position = -255
for _ in range(10):
    x_position = -255
    for _ in range(10):
        tim.setpos(x_position, y_position)
        tim.dot(20, random.choice(list_of_colors))
        x_position += 50
    y_position +=50

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# # attributes
# tim.shape("turtle")
# tim.color("red")
#
#
# colors = ["mint cream", "pale turquoise", "navy", "dodger blue", "yellow", "maroon", "violet red"]
# headings = [0, 90, 180, 270]
#
# # spirograph!
# tim.speed(0)
#
#
# def draw_spirograph(number_of_turns):
#     for _ in range(number_of_turns):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.right(360 / number_of_turns)
#
#
# draw_spirograph(10)

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
