from turtle import Turtle
MOVEMENT_INCREMENT = 10
WALL_BOUNDARY = 280

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_move = MOVEMENT_INCREMENT
        self.y_move = MOVEMENT_INCREMENT

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def check_collision(self):
        if self.ycor() > WALL_BOUNDARY:
            self.y_move = -MOVEMENT_INCREMENT

        if self.ycor() < -WALL_BOUNDARY:
            self.y_move = MOVEMENT_INCREMENT

        # if self.xcor() > WALL_BOUNDARY:
        #     self.moving_right = False
        #
        # if self.xcor() < -WALL_BOUNDARY:
        #     self.moving_right = False