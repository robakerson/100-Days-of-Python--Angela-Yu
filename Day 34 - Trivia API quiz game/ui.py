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
        self.true = Button(image=true_button, highlightthickness=0, command=self.usersel_true)
        self.false = Button(image=false_button, highlightthickness=0, command=self.usersel_false)
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
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def usersel_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def usersel_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, user_correct):
        if user_correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)

