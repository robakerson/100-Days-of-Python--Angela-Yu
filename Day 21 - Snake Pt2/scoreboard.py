from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.speed(0)
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.setpos(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))