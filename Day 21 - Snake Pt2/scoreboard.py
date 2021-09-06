from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        # self.high_score = 0
        self.hideturtle()
        self.speed(0)
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            return file.read()

    def write_high_score(self, score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.read_high_score()):
            self.write_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.setpos(0, 260)
        self.write(f"Score: {self.score} High Score: {self.read_high_score()}", align=ALIGNMENT, font=FONT)