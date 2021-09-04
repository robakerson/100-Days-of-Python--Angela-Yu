from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("black")
        self.hideturtle()
        self.setpos(-260, 260)
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", font=FONT)