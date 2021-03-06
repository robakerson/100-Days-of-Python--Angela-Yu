from turtle import Turtle
STARTING_SPEED = 10
WALL_BOUNDARY = 280

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def check_collision(self):  # reverse y direction if hit top or bottom walls
        if self.ycor() > WALL_BOUNDARY:
            self.y_move = -STARTING_SPEED

        if self.ycor() < -WALL_BOUNDARY:
            self.y_move = STARTING_SPEED

    def hit_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def score_right(self):
        self.setpos(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1

    def score_left(self):
        self.setpos(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1

    # def check_for_score(self):
    #     if self.xcor() > 350:
    #         self.score_left()
    #     if self.xcor() < -350:
    #         self.score_right()
