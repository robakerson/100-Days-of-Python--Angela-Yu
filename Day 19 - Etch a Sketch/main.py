from turtle import Turtle, Screen

#  initialize turtle & screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear_drawing():
    tim.setheading(0)
    tim.setpos(0,0)
    tim.clear()


screen.listen()
tim.speed(3)
screen.onkey(move_forwards, "w")  # onkey will call the function when space is pressed
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()