from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("POOOOONG")
screen.tracer(0)


right_paddle = Paddle(350)
left_paddle = Paddle(-350)
screen.listen()
screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")
screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(0.1)


screen.exitonclick()
