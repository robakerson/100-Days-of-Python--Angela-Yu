from turtle import Turtle, Screen
from paddle import Paddle

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("POOOOONG")
screen.tracer(0)


right_paddle = Paddle(350)
screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
