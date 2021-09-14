from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 270, image=card_front)
lang_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=1, row=1, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(column=1, row=2)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0)
correct_button.grid(column=2, row=2)


window.mainloop()