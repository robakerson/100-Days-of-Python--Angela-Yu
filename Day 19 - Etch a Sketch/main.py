from turtle import Turtle, Screen

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

# tim.up()
# # tim.shape("turtle")
# tim.setpos(-230, -100)
yposition = -75


def turtle_setup(turtle, color, yposition):  # turtle_setup makes new turtle with chosen parameters
    turtle.color(color)
    turtle.up()
    turtle.setpos(-230, yposition)


for num in range(6):  # set up 6 turtles
    turtle_setup(turtles[num], colors[num], yposition)
    yposition += 30


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