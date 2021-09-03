from turtle import Turtle
MOVEMENT_INCREMENT = 20

class Paddle:
    def __init__(self, xcor):
        self.paddle = Turtle()
        self.paddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.paddle.up()
        self.paddle.setpos(xcor, 0)
        self.paddle.shape("square")
        self.paddle.color("white")

    def paddle_up(self):
        self.paddle.setpos(self.paddle.xcor(), self.paddle.ycor() + MOVEMENT_INCREMENT)

    def paddle_down(self):
        self.paddle.setpos(self.paddle.xcor(), self.paddle.ycor() - MOVEMENT_INCREMENT)
