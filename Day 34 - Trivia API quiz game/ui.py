from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label()
        self.score.config(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=2, row=1)

        self.true_button = PhotoImage(file="images/true.png")
        self.false_button = PhotoImage(file="images/false.png")
        self.true = Button(image=self.true_button, highlightthickness=0)
        self.false = Button(image=self.false_button, highlightthickness=0)
        self.true.grid(column=1, row=4)
        self.false.grid(column=2, row=4)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.create_text(75, 100, text="HEY", font=("arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=25)

        self.window.mainloop()
