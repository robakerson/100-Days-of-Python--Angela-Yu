from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.speed(0)
        self.score = -1
        self.increase_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.setpos(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)