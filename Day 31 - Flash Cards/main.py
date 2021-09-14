from tkinter import *
from random import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# ---------------------------- Generate & Place Words! ------------------------------- #

def flip_card():
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)

def generate_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer= window.after(3000, flip_card)


fr_en = pandas.read_csv("data/french_words.csv")
words_to_learn = fr_en.to_dict(orient="records")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=1, row=1, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=1, row=2)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=generate_random_word)
correct_button.grid(column=2, row=2)

generate_random_word()

# --------------------------------------------------------------------------------- #



window.mainloop()
