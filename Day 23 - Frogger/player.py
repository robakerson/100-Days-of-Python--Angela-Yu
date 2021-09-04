from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_player(self):
        new_y_cor = self.ycor() + MOVE_DISTANCE
        self.setpos(self.xcor(), new_y_cor)

    def reset_player(self):
        self.setpos(STARTING_POSITION)

    def check_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

