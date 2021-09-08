import turtle
import pandas
from statewriter import StateWriter
# screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_writer = StateWriter()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
cur_state = states[states.state == answer_state]
# print(cur_state)
# print(cur_state["x"])

if not cur_state.empty:
    state_x_cor = int(cur_state.x)
    state_y_cor = int(cur_state.y)
    state_coordinates = (state_x_cor, state_y_cor)
    state_writer.write_state(state_coordinates, answer_state)

print(answer_state.title())

turtle.mainloop()