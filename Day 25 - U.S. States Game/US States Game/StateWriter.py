from turtle import Turtle


class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("Black")
        self.hideturtle()


    def write_state(self, coordinates):
        self.write("")
