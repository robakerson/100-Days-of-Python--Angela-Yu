from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    ball.check_collision()
    time.sleep(ball.move_speed)

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.hit_paddle()

    if ball.xcor() > 350:
        ball.score_left()
        score.l_point()
    if ball.xcor() < -350:
        ball.score_right()
        score.r_point()


screen.exitonclick()
