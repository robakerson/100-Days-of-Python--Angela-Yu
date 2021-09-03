from turtle import Turtle
MOVEMENT_INCREMENT = 20

class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.setpos(xcor, 0)
        self.shape("square")
        self.color("white")

    def paddle_up(self):
        self.setpos(self.xcor(), self.ycor() + MOVEMENT_INCREMENT)

    def paddle_down(self):
        self.setpos(self.xcor(), self.ycor() - MOVEMENT_INCREMENT)
