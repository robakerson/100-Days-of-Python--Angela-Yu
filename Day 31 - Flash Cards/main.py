from tkinter import *
from random import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- Generate & Place Words! ------------------------------- #


def replace_fr_word(word):
    canvas.itemconfig(lang_text, text="French")
    canvas.itemconfig(word_text, text=word)

def generate_random_word():
    random_word = choice(fr_en_dict_list)
    replace_fr_word(random_word["French"])

fr_en = pandas.read_csv("data/french_words.csv")
fr_en_dict_list = fr_en.to_dict(orient="records")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
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
