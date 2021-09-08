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

states_already_guessed = []  # will hold correct guesses
correct_guesses = 0  # simple track of correct guesses
while correct_guesses < 50:  # keep going until all states guessed
    answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess the State", prompt="What's another state's name?").title()
    cur_state = states[states.state == answer_state]  # grab the line from our .csv that corresponds to our guess
    if not cur_state.empty:  # if this is empty, we guessed wrong, go back to start of loop
        if answer_state not in states_already_guessed:  # do nothing if player guesses the same state twice
            states_already_guessed.append(answer_state)
            correct_guesses = len(states_already_guessed)
            state_coordinates = (int(cur_state.x), int(cur_state.y))
            state_writer.write_state(state_coordinates, answer_state)
        print(states_already_guessed)


turtle.mainloop()