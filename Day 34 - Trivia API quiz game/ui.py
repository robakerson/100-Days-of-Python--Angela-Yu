from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label()
        self.score.config(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=2, row=1)

        true_button = PhotoImage(file="images/true.png")
        false_button = PhotoImage(file="images/false.png")
        self.true = Button(image=true_button, highlightthickness=0)
        self.false = Button(image=false_button, highlightthickness=0)
        self.true.grid(column=1, row=4)
        self.false.grid(column=2, row=4)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="",
                                                     font=("arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)