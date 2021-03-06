from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAAAAAAAKE~!")
screen.tracer(0)

snake = Snake()
food = Food()

# screen listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        score.update_scoreboard()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # slice off head so it doesn't collide with itself
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()