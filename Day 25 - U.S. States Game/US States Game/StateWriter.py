from turtle import Turtle
FONT = ("courier", 12, "normal")


class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("Black")
        self.hideturtle()

    def write_state(self, coordinates, state):
        self.setpos(coordinates)
        self.write(state, align="left", font=FONT)
