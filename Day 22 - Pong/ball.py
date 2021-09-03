from turtle import Turtle
MOVEMENT_INCREMENT = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()

    def move_ball(self):
        new_x = self.xcor() + MOVEMENT_INCREMENT
        new_y = self.ycor() + MOVEMENT_INCREMENT
        self.setpos(new_x, new_y)