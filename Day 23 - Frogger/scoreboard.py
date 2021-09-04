from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("black")
        self.hideturtle()
        self.setpos(-250, 250)
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setpos(-40, 0)
        self.write("GAME OVER", font=FONT)