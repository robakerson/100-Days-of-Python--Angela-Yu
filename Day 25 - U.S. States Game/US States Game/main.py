import turtle
import pandas

# screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
cur_state = states[states.state == answer_state]
# print(cur_state)
# print(cur_state["x"])

if not cur_state.empty:
    print("Hey")

print(answer_state.title())

turtle.mainloop()